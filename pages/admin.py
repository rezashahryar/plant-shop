from django.contrib import admin

from . models import ContactUs, NewsLetter

# Register your models here.

admin.site.register(ContactUs)
admin.site.register(NewsLetter)
