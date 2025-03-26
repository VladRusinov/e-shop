from django.urls import path

from catalog import views

app_name = 'catalog'


urlpatterns = [
    path('', views.index, name='index'),
    path(
        'product/<int:product_id>/',
        views.product_detail,
        name='product_detail'
    ),
    path(
        'category/<slug:category_slug>/',
        views.category_products,
        name='category_products'
    ),
    path('catalog/', views.catalog, name='catalog'),
]
