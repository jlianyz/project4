from products.models import Product
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import CartProduct

# Create your views here.
def view_cart(request):
    cart = request.session.get('cart', {})
    # reminder: request.user is the currently logged in user
    cart = CartProduct.objects.filter(owner=request.user)
    return render(request, 'view_cart.html',{
        'cart':cart
    })