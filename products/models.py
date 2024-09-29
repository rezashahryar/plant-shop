from django.db import models

from decimal import Decimal

# Create your models here.


class Product(models.Model):
    # category
    # tags
    title = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=4, decimal_places=2)
    discount = models.IntegerField(null=True)
    slug = models.SlugField()
    image = models.ImageField(upload_to='plant-images/')
    description = models.TextField()
    plant_code = models.CharField(max_length=5)
    inventory = models.IntegerField()
    tax = models.IntegerField()

    def __str__(self) -> str:
        return self.title
    
    @property
    def price(self):
        if self.discount:
            return (self.unit_price - (self.discount / Decimal(100) * self.unit_price)).__round__(2)
        return self.unit_price
