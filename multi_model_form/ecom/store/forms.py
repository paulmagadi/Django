from django import forms
from django.forms import ModelForm
from .models import Product, ProductImage

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']

class ProductImageForm(ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']


