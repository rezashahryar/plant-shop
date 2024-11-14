from django.urls import path
from django.conf import settings

from . import views

# create your urls here


app_name = 'shop'

urlpatterns = [
    path('cart/', views.CartView.as_view(), name='cart'),
    path('add/<int:id>/', views.AddProductToCartView.as_view(), name='add_product'),
    path('remove/<str:unique_id>/', views.RemoveProductFromCart.as_view(), name='remove_product'),
    path('clear/', views.ClearTheCart.as_view(), name='clear_cart'),
    path('submit-order/', views.submit_order_view, name='submit_order'),
    path('apply/coupon/', views.apply_coupon_code, name='apply-coupon'),
    path('callback/', views.callback, name='callback'),
    path('verify-transaction/<str:token>', views.verify_transaction, name='verify_transaction'),
]

if settings.CHOOSE_PAYMENT_GATEWAY == 'zarinpal':
    urlpatterns += [
        path('payment/zarinpal/', views.zarinpal_payment, name='payment'),
        path('callback/payment', views.payment_callback_view, name='callback-zarinpal'),
    ]
