from django.db import models
from django.core.validators import validate_integer

# Create your models here.


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_num = models.CharField(max_length=11, validators=[validate_integer])
    message = models.TextField()

    def __str__(self) -> str:
        return f'{self.name} : {self.phone_num}'
