from django import forms
from django.forms import ModelForm
from .models import Product, ProductImage

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']

class ProductImageForm(ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']
        widgets = {'image': forms.FileField()}
        



# class ProductImageForm(forms.ModelForm):
#     images = MultiFileField(
#         min_num=1,  # minimum number of files required
#         max_num=10,  # maximum number of files allowed
#         max_file_size=1024*1024*5,  # 5 MB
#         required=True
    # )

    class Meta:
        model = ProductImage
        fields = ['images']


