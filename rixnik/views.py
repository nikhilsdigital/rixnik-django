from django.shortcuts import render
from store.models import Product  # Changed to Product (singular)

def home(request):
    products = Product.objects.all().filter(is_available=True)  # Corrected to Product

    context = {
        'products': products,  # Added space after the colon for consistency
    }
    return render(request, 'home.html', context)
