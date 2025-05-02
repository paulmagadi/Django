from django.shortcuts import get_object_or_404, render, redirect

from myapp.models import Product
from .forms import ProductForm
from django.contrib import messages

# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'home.html', context)

def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'product_list.html', context)

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    context = {
        'product': product,
    }
    return render(request, 'product_detail.html', context)

def add_product(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Error adding product. Please check the form.')
    return render(request, 'add_product.html', {'form': form})



def update_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Error updating product. Please check the form.')
    else:
        form = ProductForm(instance=product)
    return render(request, 'update_product.html', {'form': form, 'product': product})

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('product_list')
    else:
        messages.error(request, 'Error deleting product. Please try again.')
    return render(request, 'delete_product.html', {'product': product})