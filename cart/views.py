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
    
def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 
    messages.success(request, "Item has been added to cart!")
    request.session['cart'] = cart
    return redirect(reverse('products'))
    