from django import forms
from django.forms import ModelForm
from django.forms.fields import MultipleChoiceField

from store_app.models import Product

class ProductForm(ModelForm):
    images = MultipleChoiceField(widget=forms.FileInput(attrs={'multiple': True}))

    class Meta:
        model = Product
        fields = ['name', 'description', 'images']