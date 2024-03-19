from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSerializer

# Create your views here.
# @api_view()
# def menu_items(request):
#     items = MenuItem.objects.all()
#     return Response(items.values())

@api_view()
def menu_items(request):
    items = MenuItem.objects.all()
    serialized_items = MenuItemSerializer(items, many=True)
    return Response(serialized_items.data)