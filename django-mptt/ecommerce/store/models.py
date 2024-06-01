from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    name = models.CharField(max_length=50, verbose_name=_('Category Name'), unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = _('Categories')
    

    def __str__(self):
        return self.name
    
class Specification(models.Model):
    title = models.CharField(max_length=100, unique=True)
    Value = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = TreeForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    Specification= models.ForeignKey(Specification, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
