from django.shortcuts import get_object_or_404
from products.models import Product
from shop.models import Coupon

class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')
        # if coupon_id exist return coupon_id if not, return none
        self.coupon_id = self.session.get('coupon_id')

        if not cart:
            cart = self.session['cart'] = {}
        
        self.cart = cart


    def add(self, product, size, quantity=1):
        # generate id for each product of cart based on product_pk and size
        unique_id_product = self.generator_unique_id_product(product.pk, size)

        product_pk = str(product.pk)
        
        if unique_id_product not in self.cart:
            self.cart[unique_id_product] = {'quantity': quantity, 'size': size, 'product_pk': product.pk}
        # if replace_current_quantity:
        #     self.cart[product_pk]['quantity'] = quantity
        else:
            self.cart[unique_id_product]['quantity'] += quantity

        self.save()

    def remove_product(self, unique_id):
        if unique_id in self.cart:
            del self.cart[unique_id]
        self.save()

    def generator_unique_id_product(self, product_pk, size):
        return f'{product_pk}-{size}'

    def __iter__(self):
        cart = self.cart.copy()
        
        for item in cart.values():
            product = get_object_or_404(Product, pk=item['product_pk'])
            item['product_obj'] = product
            item['total_price'] = product.price * item['quantity']
            item['unique_id'] = self.generator_unique_id_product(product.pk, item['size'])
            yield item

    def total_price_of_cart(self):
        return sum(item['product_obj'].price * item['quantity'] for item in self.cart.values())

    def save(self):
        self.session.modified = True

    def __len__(self):
        return len(self.cart.keys())
    
    def clear(self):
        del self.session['cart']
        self.save()

    @property
    def coupon(self):
        if self.coupon_id:
            try:
                return Coupon.objects.get(id=self.coupon_id)
            except Coupon.DoesNotExist:
                pass
        return None
    
    def calculate_discount(self):
        ...
