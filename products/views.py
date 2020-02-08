from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404


# Create your views here.
def home(request):
    return render(request, 'index.html')
    
def about(request):
    return render(request, 'about.html')
    
def contact(request):
    return render(request, 'contact.html')