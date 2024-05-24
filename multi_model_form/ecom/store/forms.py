# forms.py
from django import forms
from django.forms import ModelForm
from .models import Person, Bio, Email

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

class BioForm(ModelForm):
    class Meta:
        model = Bio
        fields = ['bio', 'image']

class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = ['address']
