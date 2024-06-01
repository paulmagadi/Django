from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category, Product, Specification

class CategoryAdmin(MPTTModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)

class SpecificationAdmin(MPTTModelAdmin):
    list_display = ('title', 'parent')
    search_fields = ('title',)
    
admin.site.register(Specification, SpecificationAdmin)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)

admin.site.register(Product, ProductAdmin)


