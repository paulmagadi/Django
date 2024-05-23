from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    price =  models.DecimalField(max_digits=12, decimal_places=2)

class UploadedFile(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to='uploads/')
    
    
