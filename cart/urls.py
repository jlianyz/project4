from django.urls import path
from .views import add_to_cart, view_cart, update_cart

urlpatterns = [
   path('add/<id>', add_to_cart, name='add_to_cart'),
   path('', view_cart, name='view_cart'),
   path('update_cart/<id>', update_cart, name='update_cart')
]
