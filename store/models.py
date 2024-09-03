from django.db import models
from category.models import Category
from django.urls import reverse

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='photos/products')
    stock = models.DecimalField(max_digits=10, decimal_places=0)  # Added max_digits and decimal_places
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)  # Fixed typo
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)  # Changed to auto_now

   
    def get_url(self):
        return reverse('product_detail',args=[self.category.slug,self.slug])

    def __str__(self):
        return self.product_name
    
class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_catogery='color',is_active=True)
    
    def sizes(self):
        return super(VariationManager, self).filter(variation_catogery='size',is_active=True)


    
variation_catogery_choice=(
    ('color','color'),
    ('size','size'),
)
   
class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_catogery = models.CharField(max_length=100, choices=variation_catogery_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    objects = VariationManager()

    def __str__(self):
        return self.variation_value


