from django.db import models
from django.contrib.auth import get_user_model

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


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
