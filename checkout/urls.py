from django.urls import path, include
from .views import checkout, charge, success

urlpatterns = [
    path('', checkout, name='checkout'),
    path('charge', charge, name='charge'),
    path('success', success, name='success')
]