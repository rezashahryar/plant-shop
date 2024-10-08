import requests
import json

from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.sites.shortcuts import get_current_site


request_header = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}


def zarinpal_payment(request):
    http = 'http' if not request.is_secure() else 'https'
    payload = {
        'merchant_id': '111111111111111111111111111111111111',
        'amount': 500000,
        'description': 'sdfsdfsdf0',
        'callback_url': str(f'{http}://' + get_current_site(request).domain + reverse('products:product_list'))
    }

    res = requests.post(
        url='https://sandbox.zarinpal.com/pg/v4/payment/request.json',
        data=payload,
        # headers=request_header
    )
    authority = res.json()['data']['authority']

    return redirect(f'https://sandbox.zarinpal.com/pg/StartPay/{authority}')