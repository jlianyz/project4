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

def checkout(request):
    total_cost = calculate_cart_cost(request)
   
        
    return render(request, 'checkout.html', {
        'total_cost':total_cost/100
    })

def charge(request):
    amount = calculate_cart_cost(request)
    
    if request.method == 'GET':
        transaction = Transaction()
        transaction.owner = request.user
        transaction.cart_items = CartProduct.objects.filter(owner=request.user)
        transaction.status = "pending"
        transaction.date = timezone.now()
        transaction.save()
        
        all_cart_products = CartProduct.objects.filter(owner=request.user)
        for cart_product in all_cart_products:
            lineItem = LineItem()
            lineItem.transaction = transaction
            lineItem.product = cart_product.product
            lineItem.name = cart_product.product.name
            lineItem.cost = cart_product.product.price
            lineItem.save()
            
            
        
        order_form = OrderForm()
        payment_form = PaymentForm()
        return render(request, 'charge.html', {
            'order_form' : order_form,
            'payment_form' : payment_form,
            'amount' : amount,
            'transaction' : transaction,
            'publishable': settings.STRIPE_PUBLISHABLE_KEY
        })
    else:
        
        transaction_id = request.POST['transaction_id']
        transaction = Transaction.objects.get(pk=transaction_id)
        if transaction.status != 'pending':
             return HttpResponse (" Transaction has expired, please try again")
        
        stripeToken = request.POST['stripe_id']
        
        # set the secret key for the Stripe API
        stripe.api_key = settings.STRIPE_SECRET_KEY
        
        order_form = OrderForm(request.POST)
        payment_form = PaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount= int(request.POST['amount'])*100,
                    currency='usd',
                    description='Payment',
                    card=stripeToken
                    )
                    
                if customer.paid:
                    
                    order = order_form.save(commit=False)
                    order.date=timezone.now()
                    order.save()
                    
                   
                    
                    transaction.status ='approved'
                    transaction.save()
                    
                    #update stock quantity
                    line_items = LineItem.objects.filter(transaction_id=transaction.id)
                    for each_line_item in line_items:
                        each_line_item.product.quantity -= 1
                        each_line_item.product.save()
                    
                    cart_products = CartProduct.objects.filter(owner=request.user).delete()
                    
                    
                    return render(request, 'success.html')
                else:
                    messages.error(request, "Your card has been declined")
            except stripe.error.CardError:
                    messages.error(request, "Your card was declined!")
            
        else:
             return render(request, 'charge.html', {
            'order_form' : order_form,
            'payment_form' : payment_form,
            'amount' : amount,
            'publishable': settings.STRIPE_PUBLISHABLE_KEY
        })
        
        return render(request, 'charge.html', {
            'order_form' : order_form,
            'payment_form' : payment_form,
            'amount' : amount,
            'publishable': settings.STRIPE_PUBLISHABLE_KEY
            })