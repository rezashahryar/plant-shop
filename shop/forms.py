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

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if len(first_name) > 2:
            raise forms.ValidationError('این فیلد اجباری است')

        return first_name


class ApplyCouponForm(forms.Form):
    code = forms.CharField()
    # class Meta:
    #     model = Coupon
    #     fields = ['code']
