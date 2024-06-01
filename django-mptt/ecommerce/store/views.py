from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Specification
from .forms import ProductForm

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {'products': products})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = ProductForm()
    return render(request, 'store/create_product.html', {'form': form})

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = ProductForm(instance=product)
    return render(request, 'store/edit_product.html', {'form': form, 'product': product,})
