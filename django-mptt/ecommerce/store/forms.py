from django import forms
from mptt.forms import TreeNodeChoiceField
from .models import Product, Category, Specification

class ProductForm(forms.ModelForm):
    category = TreeNodeChoiceField(queryset=Category.objects.all())
    specification = TreeNodeChoiceField(queryset=Specification.objects.all())

    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'specification', 'color']
