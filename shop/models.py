from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MaxLengthValidator

from products.models import Product

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='orders')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    address = models.TextField()
    is_paid = models.BooleanField(default=False)

    order_note = models.TextField()

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def get_total_price_of_order(self):
        # result = 0
        # for item in self.items.all():
        #     result += item.price * item.quantity

        return sum(item.price * item.quantity for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=4, decimal_places=2)


class Coupon(models.Model):
    code = models.CharField(max_length=10, unique=True)
    valid_from = models.DateTimeField()
    valid_until = models.DateTimeField()
    discount = models.IntegerField(validators=[MinLengthValidator(1), MaxLengthValidator(100)])
    active = models.BooleanField(default=True)


class PeyGatewayTransaction(models.Model):
    # order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='transaction')
    status = models.CharField(max_length=2)
    token = models.CharField(max_length=15)
