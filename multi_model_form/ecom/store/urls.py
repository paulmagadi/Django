from django.urls import path
from .views import ProductDetailUpdateView

urlpatterns = [
    path('product/<int:pk>/edit/', ProductDetailUpdateView.as_view(), name='product_detail_update_form'),
]
