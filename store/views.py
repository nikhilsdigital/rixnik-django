from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from carts.models import CartItem
from django.db.models import Q

from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse


# View for the store page with optional category filtering
def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)

# View for displaying a specific product's detail page
def product_detail(request, category_slug, product_slug):
    try:
        # Get the single product based on category and product slug
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
        
    except Exception as e:
        # Render a custom 'product not found' template if the product does not exist
        raise e

    context = {
        'single_product': single_product,
        'in_cart'   : in_cart,
    }

    return render(request, 'store/product_detail.html', context)

def search(request):
    products = Product.objects.none()  # Default to empty queryset
    product_count = 0 

    if 'keyword' in request.GET:
        keyword = request.GET.get('keyword', '').strip()
        if keyword:
            products = Product.objects.filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()

    context = {
        'products': products,
        'product_count' : product_count,
    }
    return render(request, 'store/store.html', context)



