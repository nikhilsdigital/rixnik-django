from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# View for the store page with optional category filtering
def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)

# View for displaying a specific product's detail page
def product_detail(request, category_slug, product_slug):
    try:
        # Get the single product based on category and product slug
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        # Render a custom 'product not found' template if the product does not exist
        raise e

    context = {
        'single_product': single_product,
    }

    return render(request, 'store/product_detail.html', context)
