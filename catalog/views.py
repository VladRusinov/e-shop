from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from catalog.models import Category, Product
from users.views import get_cart_products


def index(request):
    """Главная страница"""
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'cart_products': get_cart_products(request)
        }
    return render(request, 'catalog/index.html', context)


def catalog(request):
    """Страница с каталогом товаров"""
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'catalog/catalog.html', context)


def category_products(request, category_slug):
    """Страница с товарами определенной категории"""
    category = Category.objects.get(slug=category_slug)
    products = Product.objects.filter(category=category)
    context = {
        'products': products,
        'category_title': category.title,
        'cart_products': get_cart_products(request)
    }
    return render(request, 'catalog/category_products.html', context)


def product_detail(request, product_id):
    """Страница с информацией о товаре"""
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product,
    }
    return render(request, 'catalog/product_detail.html', context)
