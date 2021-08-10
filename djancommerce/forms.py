from django import forms
from .models import *




class CartItemForm(forms.ModelForm):
    class Meta:
        model = Cartitem
        fields = ['quantity']