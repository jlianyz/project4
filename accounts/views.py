from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import MyUser
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .forms import UserLoginForm, UserRegistrationForm, UpdateDetailsForm
from django.template.context_processors import csrf

# Create your views here.
def main_account(request):
    return render(request, 'main_acct.html')
    
def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('main'))