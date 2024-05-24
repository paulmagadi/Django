from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import Product, ProductImage
from .forms import ProductForm, ProductImageForm

def product_create_view(request):
    if request.method == 'POST':
        if 'save_product' in request.POST:
            product_form = ProductForm(request.POST)
            if product_form.is_valid():
                product = product_form.save()
                messages.success(request, "Product added successfully.")
                return redirect('product_create')
            else:
                messages.error(request, "Please correct the errors below.")
        elif 'save_product_image' in request.POST:
            product_image_form = ProductImageForm(request.POST, request.FILES)
            if product_image_form.is_valid():
                product_images = product_image_form.save(commit=False)
                for product_image in product_images:
                    product_image.save()
                    product_image.product.add(product)  # Associate the image with the product
                messages.success(request, "Product image(s) added successfully.")
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
