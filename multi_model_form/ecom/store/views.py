from django.views.generic.base import TemplateView
from .models import Product, ProductImage
from .forms import ProductForm, ProductImageForm
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

class ProductDetailUpdateView(TemplateView):
    template_name = 'shop/product_detail_update_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = get_object_or_404(Product, pk=self.kwargs['pk'])
        context['product'] = product
        context['product_form'] = ProductForm(instance=product)
        context['product_image_form'] = ProductImageForm()
        context['product_images'] = ProductImage.objects.filter(product=product)
        return context
    
    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        product = get_object_or_404(Product, pk=pk)
        product_form = ProductForm(instance=product, data=request.POST)
        product_image_form = ProductImageForm(request.POST, request.FILES)
        
        if 'save_product' in request.POST:
            if product_form.is_bound and product_form.is_valid():
                product_form.save()
                messages.add_message(request, messages.SUCCESS, "Product details updated successfully.")
            else:
                messages.error(request, product_form.errors)
        
        elif 'save_product_image' in request.POST:
            if product_image_form.is_bound and product_image_form.is_valid():
                product_image = product_image_form.save(commit=False)
                product_image.product = product
                product_image.save()
                messages.add_message(request, messages.SUCCESS, "Product image added successfully.")
            else:
                messages.error(request, product_image_form.errors)
        
        return HttpResponseRedirect(reverse('shop:product_detail_update_form', kwargs={'pk': pk}))
