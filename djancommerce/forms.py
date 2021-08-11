from django import forms
from .models import *
from django.conf import settings


class CartItemForm(forms.ModelForm):
    class Meta:
        model = Cartitem
        fields = ['quantity']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment_method', 'delivery_method']
        widgets = {
            'payment_method': forms.Select(choices=settings.PAYMENT_METHODS),
            'delivery_method': forms.Select(choices=settings.PAYMENT_METHODS),
                   }