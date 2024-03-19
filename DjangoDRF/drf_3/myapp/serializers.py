from rest_framework import serializers
from .models import MenuItem, Category
from decimal import Decimal




# class MenuItemSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     price = serializers.DecimalField(max_digits=8, decimal_places=2)
#     inventory = serializers.IntegerField()
    


# # MODEL SERIALIZERS
# class MenuItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MenuItem
#         fields = ['id', 'title', 'price', 'inventory']
    
  
  #CREATE A NEW FIELD
# class MenuItemSerializer(serializers.ModelSerializer):
#   stock = serializers.IntegerField(source='inventory')
#   class Meta:
#     model = MenuItem
#     fields = ['id', 'title', 'price', 'stock']
  
  
  
# class MenuItemSerializer(serializers.ModelSerializer):
#   category = serializers.StringRelatedField()
#   stock = serializers.IntegerField(source='inventory')
#   price_after_tax = serializers.SerializerMethodField(method_name= 'calculate_tax')
#   class Meta:
#       model = MenuItem
#       fields = ['id','category', 'title', 'price', 'stock', 'price_after_tax']  
      
#   def calculate_tax(self, product:MenuItem):
#     return product.price * Decimal(1.1)



class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['id', 'slug', 'title']
  
  
class MenuItemSerializer(serializers.ModelSerializer):
  category = CategorySerializer()
  category = CategorySerializer(read_only=True)
  stock = serializers.IntegerField(source='inventory')
  price_after_tax = serializers.SerializerMethodField(method_name= 'calculate_tax')
  class Meta:
      model = MenuItem
      fields = ['id','category', 'title', 'price', 'stock', 'price_after_tax']  
      
  def calculate_tax(self, product:MenuItem):
    return product.price * Decimal(1.1)
      
    
      