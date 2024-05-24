from django.db import models

# Create your models here.


class UploadedFile(models.Model):
    file = models.FileField(upload_to='products/')