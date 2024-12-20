from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View, generic
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

from products.models import Product
from shop.models import Coupon, OrderItem

from shop.forms import ApplyCouponForm, OrderForm
from shop.cart import Cart

# Create your views here.

def callback_gateway(request):
    return redirect('pages:home')


class CartView(LoginRequiredMixin, generic.FormView):
    template_name = 'shop/cart.html'
    form_class = OrderForm
    success_url = reverse_lazy('shop:payment')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)

        return context
    
    def form_invalid(self, form):
        cart = Cart(self.request)
        if len(cart) == 0:
            messages.warning(self.request, 'your cart is empty, so please for order first choose product')
            return redirect('products:product_list')
        response = super().form_invalid(form)
        return response
    
    
    def form_valid(self, form):
        cart = Cart(self.request)
        if len(cart) == 0:
            messages.warning(self.request, 'your cart is empty, so please for order first choose product')
            return redirect('products:product_list')
        
        order_form_obj = form.save(commit=False)
        order_form_obj.user = self.request.user
        order_form_obj.save()
        # save order item from items of cart
        for item in cart:
            OrderItem.objects.create(
                order_id=order_form_obj.pk,
                product_id=item['product_obj'].pk,
                quantity=item['quantity'],
                price=item['product_obj'].price,
            )

            item['product_obj'].inventory -= item['quantity']
            item['product_obj'].save()

        cart.clear()

        self.request.session['order_id'] = order_form_obj.pk
        
        return super().form_valid(form)
    


class AddProductToCartView(View):

    def post(self, request, id):
        cart = Cart(request)
        product_obj = get_object_or_404(Product, pk=id)

        quantity = int(request.POST['quantity'])
        
        size = request.POST.get('size')
        if not size:
            size = product_obj.sizes.all()[0].name

        cart.add(product_obj, size, quantity)
        messages.success(request, 'add product to your cart')

        return redirect('shop:cart')
    

class RemoveProductFromCart(View):

    def post(self, request, unique_id):
        cart = Cart(request)

        cart.remove_product(unique_id)
        messages.success(request, 'DONE!')
        return redirect('shop:cart')
    

class ClearTheCart(View):

    def post(self, request):
        cart = Cart(request)
        if len(cart):
            cart.clear()
        else:
            messages.warning(request, 'your cart is already empty')
        return redirect('shop:cart')
    

@require_POST
@login_required
def submit_order_view(request):
    order_form = OrderForm(request.POST)
    cart = Cart(request)

    if len(cart) == 0:
        messages.warning(request, 'your cart is empty, so please for order first choose product')
        return redirect('products:product_list')

    if order_form.is_valid():
        order_form_obj = order_form.save(commit=False)
        order_form_obj.user = request.user
        order_form_obj.save()
        # save order item from items of cart
        for item in cart:
            OrderItem.objects.create(
                order_id=order_form_obj.pk,
                product_id=item['product_obj'].pk,
                quantity=item['quantity'],
                price=item['product_obj'].price,
            )

            item['product_obj'].inventory -= item['quantity']
            item['product_obj'].save()

        cart.clear()

        # return redirect('shop:payment_idpay', order_form_obj.pk)

        return redirect('shop:payment', order_form_obj.pk)
    return render(request, 'shop/cart.html', {'order_form': order_form})


@require_POST
def apply_coupon_code(request):
    datetime_now = timezone.now()
    form = ApplyCouponForm(request.POST)

    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon_obj = Coupon.objects.get(code=code, valid_from__lte=datetime_now, valid_until__gte=datetime_now, active=True)
            request.session['coupon_id'] = coupon_obj.pk
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
        
    return redirect('shop:cart')
