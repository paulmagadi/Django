from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price =  models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/products')
