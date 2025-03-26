from django.urls import path

from users import views

app_name = 'users'


urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path(
        'add_to_shopping_cart/<int:product_id>/',
        views.add_to_shopping_cart,
        name='add_to_shopping_cart'
    ),
    path(
        'shopping_cart/<int:user_id>/',
        views.shopping_cart,
        name='shopping_cart'
    ),
    path(
        'remove_from_shopping_cart/<int:product_id>/',
        views.remove_from_shopping_cart,
        name='remove_from_shopping_cart'
    )
]
