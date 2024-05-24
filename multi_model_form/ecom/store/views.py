from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import Product, ProductImage
from .forms import ProductForm, ProductImageForm

def product_create_view(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        product_image_form = ProductImageForm(request.POST, request.FILES)
        
        if product_form.is_valid() and product_image_form.is_valid():
            product = product_form.save()
            product_image = product_image_form.save(commit=False)
            product_image.product = product
            product_image.save()
            messages.success(request, "Product and image added successfully.")
            return redirect('product_create')
        else:
            messages.error(request, "Please correct the errors below.")
    
    else:
        product_form = ProductForm()
        product_image_form = ProductImageForm()

    return render(request, 'home.html', {
        'product_form': product_form,
        'product_image_form': product_image_form
    })
