from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    images = models.ImageField(upload_to='products/', blank=True, null=True)