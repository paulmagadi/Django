from django.shortcuts import render, redirect
from .models import Product, ProductImage
from .forms import ProductForm, ProductImageForm
from django.contrib import messages

def home(request):
    return render(request, 'index.html')

def product_create_view(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        product_image_form = ProductImageForm(request.POST, request.FILES)
        
        if product_form.is_valid() and product_image_form.is_valid():
            product = product_form.save()
            images = request.FILES.getlist('images')
            for image in images:
                ProductImage.objects.create(product=product, image=image)
            
            messages.success(request, 'Product and images saved successfully!')
            return redirect('home')  
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        product_form = ProductForm()
        product_image_form = ProductImageForm()

    return render(request, 'home.html', {
        'product_form': product_form,
        'product_image_form': product_image_form
    })
