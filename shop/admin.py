from django.contrib import admin

from .models import Order, OrderItem, Coupon, PeyGatewayTransaction

# Register your models here.


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['valid_from', 'valid_until', 'discount', 'active']
    list_filter = ['valid_from', 'valid_until', 'active']
    search_fields = ['code']


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


@admin.register(PeyGatewayTransaction)
class PeyGatewayTransactionAdmin(admin.ModelAdmin):
    ...
