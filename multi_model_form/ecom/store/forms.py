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

class ProductImageForm(forms.Form):
    images = MultipleFileField()

    def clean_images(self):
        images = self.files.getlist('images')
        if len(images) > 5:  
            raise forms.ValidationError('You can upload a maximum of 5 images.')
        return images


    


