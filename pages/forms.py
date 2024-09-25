from django import forms

from .models import ContactUs

# create your forms here


class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'phone_num', 'message']
