from products.models import Product
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import CartProduct


# Create your views here.
def view_cart(request):
    if request.user:
       # reminder: request.user is the currently logged in user
        return render(request, 'view_cart.html')


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


def update_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
