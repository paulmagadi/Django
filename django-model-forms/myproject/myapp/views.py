from django.shortcuts import render, redirect
from .forms import ProductForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def product(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'product.html', {'form': form})