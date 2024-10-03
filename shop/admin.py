from django.contrib import admin

from .models import Order, OrderItem

# Register your models here.


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    ...


class OrderItemTabularInline(admin.TabularInline):
    model = OrderItem
    fields = ['product', 'quantity', 'price']
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemTabularInline]
