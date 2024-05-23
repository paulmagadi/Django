from django.contrib import admin
from .models import UploadedFile, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(UploadedFile)