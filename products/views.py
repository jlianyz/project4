from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def bakers(request):
    return render(request, 'bakers.html')


def contact(request):
    return render(request, 'contact.html')


def product_list(request):
    products = Product.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(products, 9)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'product_list.html', {
        'products': products
    })

# allow search by typing any part of the word
def search_products(request):
    product = Product.objects.filter(name__icontains=request.GET['query'])
    return render(request, "product_list.html", {'products': product})


def product_details(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'product_details.html', {
        'product': product
    })


def filter_products(request, category):

    if category == "Cake pops":
        product_category = Product.objects.filter(category='Cake pops')
    elif category == "Chocolates":
        product_category = Product.objects.filter(category='Chocolates')
    elif category == "Macarons":
        product_category = Product.objects.filter(category='Macarons')
    elif category == "Pastries":
        product_category = Product.objects.filter(category='Pastries')
    elif category == "Cookies":
        product_category = Product.objects.filter(category='Cookies')
    elif category == "Brownies":
        product_category = Product.objects.filter(category='Brownies')
    elif category == "Cupcakes":
        product_category = Product.objects.filter(category='Cupcakes')
    elif category == "Tarts":
        product_category = Product.objects.filter(category='Tarts')

    return render(request, "product_list.html", {
        'products': product_category
    })
