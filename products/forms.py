from django import forms

# create your forms here


class SearchByPriceProductForm(forms.Form):
    price1 = forms.IntegerField()
    price2 = forms.IntegerField()
