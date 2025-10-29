from django.urls import path
from product.views import get_home, get_about, get_product

urlpatterns = [
    path('', get_home, name='home'),
    path('about/', get_about, name='about'),
    path('product/', get_product, name='list-product'),
]