from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/add/', views.create_product, name='create_product'),
    path('product/edit/<int:pk>/', views.edit_product, name='edit_product'),
]