from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):  # Changed from models.Model to admin.ModelAdmin
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}  # Automatically populate the slug field

admin.site.register(Product, ProductAdmin)
