from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'slug', 'price', 'stock', 'category_id', 'is_available', 'modified')

admin.site.register(Product, ProductAdmin)