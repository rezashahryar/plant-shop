from django import forms

from .models import Order

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

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit():
            raise forms.ValidationError('شماره تلفن تماما باید عددی باشد')
        return phone_number


class ApplyCouponForm(forms.Form):
    code = forms.CharField()
