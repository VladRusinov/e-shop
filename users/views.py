from django.shortcuts import get_object_or_404, redirect, render

from catalog.models import Product
from users.models import ShoppingCart


def profile(request):
    """Личный кабинет пользователя."""
    user = request.user
    if user.is_authenticated:
        context = {"user": user}
        return render(request, 'users/profile.html', context)
    return redirect('login')


def add_to_shopping_cart(request, product_id):
    """Добавить товар в корзину."""
    user = request.user
    if user.is_authenticated:
        product = get_object_or_404(Product, id=product_id)
        ShoppingCart.objects.get_or_create(user=user, product=product)
        return redirect(request.META.get('HTTP_REFERER', '/'))
    return redirect('login')


def remove_from_shopping_cart(request, product_id):
    """Удалить товар из корзины."""
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    cart_item = ShoppingCart.objects.filter(
        user=user,
        product=product_id
    )
    if cart_item.exists():
        cart_item.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))


def get_cart_products(request):
    """Функция для получения товаров в корзине."""
    if request.user.is_authenticated:
        return set(
            ShoppingCart.objects.filter(
                user=request.user
            ).values_list('product_id', flat=True)
        )
    return set()


def shopping_cart(request, user_id):
    """Корзина."""
    user = request.user
    products = Product.objects.filter(shopping_carts__user=user_id)
    context = {
        "products": products,
        "user": user,
        "cart_products": get_cart_products(request),
    }
    return render(request, 'users/shopping_cart.html', context)
