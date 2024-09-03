from django.contrib import admin
from .models import Product, Variation

class ProductAdmin(admin.ModelAdmin):  # Changed from models.Model to admin.ModelAdmin
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}  # Automatically populate the slug field
class VariationAdmin(admin.ModelAdmin):
    list_display = ('product','variation_catogery','variation_value','is_active')
    list_editable = ('is_active',)
    list_filter = ('product','variation_catogery','variation_value')

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
