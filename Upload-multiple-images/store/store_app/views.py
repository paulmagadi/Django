from django.shortcuts import render

from django.views.generic import CreateView

from store_app.forms import ProductForm
from store_app.models import Product

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_create.html'
