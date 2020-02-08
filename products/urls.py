from django.urls import path
from .views import home, product_list, search_products, product_details, filter_products

urlpatterns = [
    path('', home, name="index"),
    path('products/', product_list, name="products"),
    path('result/', search_products, name="search"),
    path('details/<id>', product_details, name="details"),
    path('filter/<category>', filter_products, name="filter"),
]
