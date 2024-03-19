from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
    
class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory = models.SmallIntegerField()
    
def __str__(self):
        return self.title