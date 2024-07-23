from django import forms
from zayapp.models import Products


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name' , 'description' , 'price' , 'category' , 'season' ,  'quantity' , 'image']