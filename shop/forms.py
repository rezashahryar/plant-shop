from django import forms

from .models import Coupon, Order

# create your forms here


class AddToCartProductForm(forms.Form):
    QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 31)]

    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES, coerce=int)


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [
            'first_name', 'last_name', 'email', 'phone_number', 'address', 'order_note'
        ]


class ApplyCouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = ['code']
