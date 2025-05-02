from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('product/add', views.add_product, name='add_product'),
    path('product/update/<int:id>/', views.update_product, name='update_product'),
    path('product/delete/<int:id>/', views.delete_product, name='delete_product'),
    
]