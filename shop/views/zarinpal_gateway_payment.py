import requests

from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse

from shop.models import Order, ZarinpalGatewayTransaction


def zarinpal_payment(request):
    order_id = request.session.get('order_id')
    order_obj = get_object_or_404(Order, id=order_id)

    # request.session['order_id'] = order_id
    
    payload = {
        'merchant_id': '111111111111111111111111111111111111',
        'amount': int(order_obj.get_total_price_of_order()),
        'description': 'sdfsdfsdf0',
        'callback_url': request.build_absolute_uri(reverse('shop:callback-zarinpal'))
    }

    res = requests.post(
        url='https://sandbox.zarinpal.com/pg/v4/payment/request.json',
        data=payload,
    )

    if 'errors' not in res.json() or len(res.json()['errors']) == 0:
        data = res.json()['data']
        authority = data['authority']
        ZarinpalGatewayTransaction.objects.create(
            order_id=order_id,
            authority=authority
        )
        return redirect(f'https://sandbox.zarinpal.com/pg/StartPay/{authority}')
    else:
        return HttpResponse('error from zarinpal')
    

def payment_callback_view(request):
    order_obj = get_object_or_404(Order, id=request.session.get('order_id'))

    authority = request.GET.get('Authority')
    Status = request.GET.get('Status')
    zarinpal_gateway_transaction_obj = ZarinpalGatewayTransaction.objects.get(authority=authority)

    payload = {
        'merchant_id': '111111111111111111111111111111111111',
        'amount': int(order_obj.get_total_price_of_order()),
        'authority': authority,
    }

    res = requests.post(
        url='https://sandbox.zarinpal.com/pg/v4/payment/verify.json',
        data=payload,
    )

    if 'data' in res.json() and ('errors' not in res.json()['data'] or len(res.json()['data']['errors']) == 0):
        data = res.json()['data']
        payment_status_code = data.get('code')

        if payment_status_code == 100:
            zarinpal_gateway_transaction_obj.order.is_paid = True
            zarinpal_gateway_transaction_obj.order.save()
            zarinpal_gateway_transaction_obj.ref_id = data['ref_id']
            zarinpal_gateway_transaction_obj.zarinpal_data = data
            zarinpal_gateway_transaction_obj.save()

            return HttpResponse('سفارش شما با موفقیت انجام شد')
        elif payment_status_code == 101:
            return HttpResponse('پرداخت شما با موفقیت انجام شد ، البته این تراکنش قبلا انجام شده است.')
        

    return HttpResponse('تراکنش ناموفق بود')
