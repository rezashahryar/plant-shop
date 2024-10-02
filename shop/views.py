from django.shortcuts import get_object_or_404, redirect, render
from django.views import View, generic
from django.contrib import messages

from products.models import Product

from .forms import AddToCartProductForm
from .cart import Cart

# Create your views here.


class CartView(generic.ListView):
    template_name = 'shop/cart.html'
    context_object_name = 'cartt'

    def get_queryset(self):
        cart = Cart(self.request)
        return cart


class AddProductToCartView(View):

    def post(self, request, id):
        cart = Cart(request)
        product_obj = get_object_or_404(Product, pk=id)

        quantity = int(request.POST['quantity'])

        cart.add(product_obj, quantity)
        messages.success(request, 'add product to your cart')

        return redirect('shop:cart')
    

class RemoveProductFromCart(View):

    def post(self, request, pk):
        cart = Cart(request)
        product_obj = get_object_or_404(Product, pk=pk)

        cart.remove_product(product_obj)
        messages.success(request, 'DONE!')
        return redirect('shop:cart')
    

class ClearTheCart(View):

    def post(self, request):
        cart = Cart(request)
        cart.clear()
        return redirect('shop:cart')
