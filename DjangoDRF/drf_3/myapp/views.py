from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from .models import MenuItem, Category
from .serializers import MenuItemSerializer
from rest_framework import status
from  decimal import Decimal
from django.core.paginator import Paginator, EmptyPage

from rest_framework.permissions import IsAuthenticated

from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

from .throttle import TenCallsPerMinute

from rest_framework.permissions import IsAdminUser



# Create your views here.
# @api_view()
# def menu_items(request):
#     items = MenuItem.objects.all()
#     return Response(items.values())

# @api_view()
# def menu_items(request):
#     items = MenuItem.objects.all()
#     serialized_items = MenuItemSerializer(items, many=True)
#     return Response(serialized_items.data)

# @api_view()
# def menu_items(request):
#     items = MenuItem.objects.select_related('category').all()
#     serialized_items = MenuItemSerializer(items, many=True)
#     return Response(serialized_items.data)

# @api_view()
# def menu_item(request, id):
#     item = MenuItem.objects.get(pk=id)
#     serialized_item = MenuItemSerializer(item)
#     return Response(serialized_item.data)

# @api_view()
# def menu_item(request, id):
#     item = get_object_or_404(MenuItem,pk=id)
#     serialized_item = MenuItemSerializer(item)
#     return Response(serialized_item.data)


#DESERIALIZATION

# @api_view(['GET', 'POST'])
# def menu_items(request):
#     if request.method == 'GET':
#         items = MenuItem.objects.select_related('category').all()
#         serialized_items = MenuItemSerializer(items, many=True)
#         return Response(serialized_items.data)
#     if request.method == 'POST':
#         serialized_items = MenuItemSerializer(data=request.data)
#         serialized_items.is_valid(raise_exception=True)
#         serialized_items.save()
#         return Response(serialized_items.data, status.HTTP_201_CREATED)



# @api_view()
# def menu_item(request, id):
#     item = get_object_or_404(MenuItem,pk=id)
#     serialized_item = MenuItemSerializer(item)
#     return Response(serialized_item.data)


# #search query/ filter
# @api_view(['GET', 'POST'])
# def menu_items(request):
#     if request.method == 'GET':
#         items = MenuItem.objects.select_related('category').all()
#         category_name = request.query_params.get('category')
#         to_price = request.query_params.get('to_price')
#         if category_name:
#             items = items.filter(category__title=category_name)
#         if to_price:
#             items = items.filter(price__lte=to_price)
#         serialized_items = MenuItemSerializer(items, many=True)
#         return Response(serialized_items.data)
#     if request.method == 'POST':
#         serialized_items = MenuItemSerializer(data=request.data)
#         serialized_items.is_valid(raise_exception=True)
#         serialized_items.save()
#         return Response(serialized_items.data, status.HTTP_201_CREATED)


#search
# @api_view(['GET', 'POST'])
# def menu_items(request):
#     if request.method == 'GET':
#         items = MenuItem.objects.select_related('category').all()
#         category_name = request.query_params.get('category')
#         to_price = request.query_params.get('to_price')
#         search = request.query_params.get('search')
#         if category_name:
#             items = items.filter(category__title=category_name)
#         if to_price:
#             items = items.filter(price__lte=to_price)
#         if search:
#             items = items.filter(title__contains=search)
#             # items = items.filter(title__startswith=search)   #Case insensitive
#         serialized_items = MenuItemSerializer(items, many=True)
#         return Response(serialized_items.data)
#     if request.method == 'POST':
#         serialized_items = MenuItemSerializer(data=request.data)
#         serialized_items.is_valid(raise_exception=True)
#         serialized_items.save()
#         return Response(serialized_items.data, status.HTTP_201_CREATED)

@api_view()
def menu_item(request, id):
    item = get_object_or_404(MenuItem,pk=id)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)


# ordering

# @api_view(['GET', 'POST'])
# def menu_items(request):
#     if request.method == 'GET':
#         items = MenuItem.objects.select_related('category').all()
#         category_name = request.query_params.get('category')
#         to_price = request.query_params.get('to_price')
#         search = request.query_params.get('search')
#         ordering = request.query_params.get('ordering')
#         if category_name:
#             items = items.filter(category__title=category_name)
#         if to_price:
#             items = items.filter(price__lte=to_price)
#         if search:
#             items = items.filter(title__contains=search)
#             # items = items.filter(title__startswith=search)   #Case insensitive
#         if ordering:
#             # items = items.order_by(ordering)
#             ordering_fields = ordering.split(",")
#             items = items.order_by(*ordering_fields)
#         serialized_items = MenuItemSerializer(items, many=True)
#         return Response(serialized_items.data)
#     if request.method == 'POST':
#         serialized_items = MenuItemSerializer(data=request.data)
#         serialized_items.is_valid(raise_exception=True)
#         serialized_items.save()
#         return Response(serialized_items.data, status.HTTP_201_CREATED)
    
    
#pagination

@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
        perpage = request.query_params.get('perpage', default=2)
        page = request.query_params.get('page', default=1)
        if category_name:
            items = items.filter(category__title=category_name)
        if to_price:
            items = items.filter(price__lte=to_price)
        if search:
            items = items.filter(title__contains=search)
            # items = items.filter(title__startswith=search)   #Case insensitive
        if ordering:
            # items = items.order_by(ordering)
            ordering_fields = ordering.split(",")
            items = items.order_by(*ordering_fields)
        paginator = Paginator(items, per_page=perpage)
        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items = []
        serialized_items = MenuItemSerializer(items, many=True)
        return Response(serialized_items.data)
    if request.method == 'POST':
        serialized_items = MenuItemSerializer(data=request.data)
        serialized_items.is_valid(raise_exception=True)
        serialized_items.save()
        return Response(serialized_items.data, status.HTTP_201_CREATED)
    
    
    #token authentification
    
@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message":"Secrete message"})


@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name='Manager').exists():
        return Response({"message":"Only managers "})
    else:
        return Response({"message":"You are not authorized "}, 403)
    
    
@api_view()  
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({"message":"sucessfull"})


# @api_view()  
# @permission_classes([IsAuthenticated])
# @throttle_classes([UserRateThrottle])
# def throttle_check_auth(request):
#     return Response({"message":"sucessfull"})


@api_view()  
@permission_classes([IsAuthenticated])
@throttle_classes([TenCallsPerMinute])
def throttle_check_auth(request):
    return Response({"message":"sucessfull"})
    
    
    
@api_view()  
@permission_classes([IsAdminUser])
def managers(request):
    return Response({"message": "ok"})