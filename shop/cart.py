from products.models import Product

class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}
        
        self.cart = cart


    def add(self, product, quantity=1):
        product_pk = str(product.pk)
        
        if product_pk not in self.cart:
            self.cart[product_pk] = {'quantity': quantity}
        # if replace_current_quantity:
        #     self.cart[product_pk]['quantity'] = quantity
        else:
            self.cart[product_pk]['quantity'] += quantity

        self.save()

    def remove_product(self, product):
        product_pk = str(product.pk)
        if product_pk in self.cart:
            del self.cart[product_pk]
        self.save()

    # def __iter__(self):

    #     for item in self.cart:
    #         yield item

    def __iter__(self):
        list_id_of_products = self.cart.keys()
        products = Product.objects.filter(id__in=list_id_of_products)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.pk)]['product_obj'] = product
            cart[str(product.pk)]['total_price'] = product.price * cart[str(product.pk)]['quantity']
        
        for item in cart.values():
            yield item

    def save(self):
        self.session.modified = True

    def __len__(self):
        return len(self.cart.keys())
    
    def clear(self):
        del self.session['cart']
        self.save()
