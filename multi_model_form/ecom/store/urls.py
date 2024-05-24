from django.urls import path
from . import views
from .views import  product_create_view

urlpatterns = [
    path('products/', product_create_view, name='product_create'),
    path('', views.home, name='home'),
]
