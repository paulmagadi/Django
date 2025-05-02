from django import forms
from .models import Product

# This is a Django form for the Product model.
# It includes fields for name, description, price, and stock.
# The form uses widgets to customize the appearance of the fields in HTML.
# It also includes labels, help texts, and error messages for better user experience.
# The clean methods are used to validate the data entered by the user.

# This form is used to create or update a product in the database.
# It inherits from forms.ModelForm, which is a built-in Django form class for model forms.
# The Meta class is used to specify the model and fields that the form will use.
# The widgets dictionary is used to customize the appearance of the form fields in HTML.
# The labels dictionary is used to specify the labels for the form fields.
# The help_texts dictionary is used to provide additional information about the fields.
# The error_messages dictionary is used to specify custom error messages for validation errors.
# The clean methods are used to validate the data entered by the user and raise validation errors if necessary.

# The clean methods are called automatically when the form is validated.
# They are used to perform custom validation on the form fields.
# The cleaned_data dictionary contains the validated data for the form fields.
# The clean methods return the cleaned data, which is then used to save the form to the database.

# The clean methods can raise ValidationError exceptions if the data is not valid.
# The ValidationError exception is a built-in Django exception that is used to indicate that the data entered by the user is not valid.

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Product Description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Stock'}),
        } 
        labels = {
            'name': 'Product Name',
            'description': 'Product Description',
            'price': 'Price',
            'stock': 'Stock',
        }
        help_texts = {
            'name': 'Enter the name of the product.',
            'description': 'Enter a brief description of the product.',
            'price': 'Enter the price of the product.',
            'stock': 'Enter the available stock for the product.',
        }  
        error_messages = {
                'name': {
                    'required': "Please enter the product name.",
                    'max_length': "Product name is too long.",
                },
                'description': {
                    'required': "Please enter the product description.",
                    'max_length': "Product description is too long.",
                },
                'price': {
                    'required': "Please enter the price.",
                    'invalid': "Enter a valid number.",
                },
                'stock': {
                    'required': "Please enter the stock amount.",
                    'invalid': "Enter a valid number.",
                },
        }

        def clean_name(self):
            name = self.cleaned_data.get('name')
            if not name:
                raise forms.ValidationError("Name is required.")
            return name
        
        def clean_price(self):
            price = self.cleaned_data.get('price')
            if price <= 0:
                raise forms.ValidationError("Price must be greater than zero.")
            return price

        def clean_stock(self):
                stock = self.cleaned_data.get('stock')
                if stock < 0:
                    raise forms.ValidationError("Stock cannot be negative.")
                return stock
    