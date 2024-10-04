from django.urls import path

# from views.payment_views import go_to_gateway_view

from . import views
from .payment_views import go_to_gateway_view

# create your urls here


app_name = 'shop'

urlpatterns = [
    path('cart/', views.CartView.as_view(), name='cart'),
    path('add/<int:id>/', views.AddProductToCartView.as_view(), name='add_product'),
    path('remove/<int:pk>/', views.RemoveProductFromCart.as_view(), name='remove_product'),
    path('clear/', views.ClearTheCart.as_view(), name='clear_cart'),
    path('submit-order/', views.submit_order_view, name='submit_order'),
    path('payment/', go_to_gateway_view, name='payment'),
    path('callback-gateway/', views.callback_gateway, name='callback-gateway')
]
