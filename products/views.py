from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    return render(request, 'index.html')
    
def about(request):
    return render(request, 'about.html')
    
def contact(request):
    return render(request, 'contact.html')
    
def product_list(request):
    products = Product.objects.all();
    
    page = request.GET.get('page', 1)

    paginator = Paginator(products, 9)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'product_list.html',{
        'products':products
    })