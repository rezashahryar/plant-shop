import requests
import json

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages

from shop.models import Order, PeyGatewayTransaction

# create your views here

request_header = {
    'accept': 'application/json',
    'content_type': 'application/json',
}

DOLLOR_TO_TOMAN = 58000


def pay_payment_gateway(request, order_id):
    # get order obj from url param
    order_obj = get_object_or_404(Order, id=order_id)
    # calculate total price of order based on rial and toman unit money
    toman_total_price_of_order = order_obj.get_total_price_of_order() * DOLLOR_TO_TOMAN
    rial_total_price_of_order = order_obj.get_total_price_of_order() * DOLLOR_TO_TOMAN * 10

    payload = {
        'api': 'test',
        'amount': rial_total_price_of_order,
        'mobile': '09050236353',
        'redirect': get_current_site(request).domain + reverse('shop:callback'),
    }

    res= requests.post(
        url='https://pay.ir/pg/send',
        data=payload,
        headers=request_header,
    )
    token = res.json()['token']
    return redirect(f'https://pay.ir/pg/{token}')


def callback(request):
    status = request.GET['status']
    token = request.GET['token']

    PeyGatewayTransaction.objects.create(status=status, token=token)

    return redirect('shop:verify_transaction', token)


def verify_transaction(request, token):
    url = 'https://pay.ir/pg/verify'
    payload = {
        'api': 'test',
        'token': token,
    }

    res = requests.post(
        url=url,
        data=payload
    )
    
    if res.status_code == 200:
        messages.success(request, 'تراکنش موفقیت آمیز بود')
    elif res.status_code == 422:
        messages.warning(request, 'تراکتش ناموفق بود')
    return redirect('pages:home')
