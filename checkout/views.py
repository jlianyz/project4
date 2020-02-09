from django.shortcuts import render, HttpResponse, reverse, redirect
from .forms import OrderForm, PaymentForm
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from cart.models import CartProduct
from .models import Charge, Transaction, LineItem
from products.models import Product
import stripe


def calculate_cart_cost(request):
    all_cart_products = CartProduct.objects.filter(owner=request.user)
    amount = 0
    for cart_product in all_cart_products:
        amount += cart_product.product.price * cart_product.quantity
        
    return amount