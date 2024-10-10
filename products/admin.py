from django.contrib import admin

from .models import Product, ProductImage, Size, Color, CategoryProduct, TagProduct

# Register your models here.


@admin.register(TagProduct)
class TagProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


@admin.register(CategoryProduct)
class CategoryProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'unit_price', 'discount', 'price', 'tax', 'product_code', 'inventory']
    # list_filter = ['unit_price']
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ['product_code']

    def price(self, obj):
        return obj.price


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    ...


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    ...


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    ...
