from django.db import models

class Person(models.Model):
    name =  models.CharField(max_length=255)

class Bio(models.Model):
    description = models.TextField()

class Email(models.Model):
    email = models.EmailField()
    