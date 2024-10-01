from django import forms

from .models import ContactUs, NewsLetter

# create your forms here


class SubscribeNewsLetterForm(forms.ModelForm):

    class Meta:
        model = NewsLetter
        fields = ['email']


class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'phone_num', 'message']
