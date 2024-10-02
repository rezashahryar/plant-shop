from django.urls import path

from . import views

# create your urls here


app_name = 'shop'

urlpatterns = [
    path('cart/', views.CartView.as_view(), name='cart'),
    path('add/<int:id>/', views.AddProductToCartView.as_view(), name='add_product'),
    path('remove/<int:pk>/', views.RemoveProductFromCart.as_view(), name='remove_product'),
    path('clear/', views.ClearTheCart.as_view(), name='clear_cart'),
]

