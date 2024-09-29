from django.db import models
from django.urls import reverse

from decimal import Decimal

# Create your models here.


class Product(models.Model):
    # category
    # tags
    title = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=4, decimal_places=2)
    discount = models.IntegerField(null=True)
    slug = models.SlugField()
    cover = models.ImageField(upload_to='plant-covers/')
    description = models.TextField()
    product_code = models.CharField(max_length=5)
    inventory = models.IntegerField()
    tax = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("products:product_detail", kwargs={"slug": self.slug})
    
    @property
    def price(self):
        if self.discount:
            return (self.unit_price - (self.discount / Decimal(100) * self.unit_price)).__round__(2)
        return self.unit_price
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product-images/')
