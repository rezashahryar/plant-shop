from django.contrib import admin

from .models import Product, ProductImage

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    ...
