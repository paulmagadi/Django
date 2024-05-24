from django import forms
from django.forms import ModelForm
from .models import Product, ProductImage
from multifilefield.fields import MultiFileField

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']

# class ProductImageForm(ModelForm):
#     class Meta:
#         model = ProductImage
#         fields = ['image']
#         widgets = {'image': forms.FileInput(attrs={'multiple': True})}
        



class ProductImageForm(forms.ModelForm):
    images = MultiFileField(
        min_num=1,  # minimum number of files required
        max_num=10,  # maximum number of files allowed
        max_file_size=1024*1024*5,  # 5 MB
        required=True
    )

    class Meta:
        model = ProductImage
        fields = ['images']


