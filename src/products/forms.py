from django import forms
from .models import Purchase, Product

class PurchaseForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all(),
                                    label='Product',
                                    widget=forms.Select(attrs={'class': 'ui selection dropdown field-with'}))
    class Meta:
        model = Purchase
        fields = ['product', 'price', 'quantity']