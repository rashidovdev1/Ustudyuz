from django.urls import path

from product.views import get_products, create_product

urlpatterns = [
    path('', get_products, name='list'),
    path('create/', create_product, name='create'),
]