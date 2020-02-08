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

def login(request):
    """Returns the login page"""
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST) # populate the form from what the user has keyed in
        if login_form.is_valid():
            # attempt to check the username and password is valid
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            messages.success(request, "You have successfully logged in")
            if user:
                # log in the user
                auth.login(user=user, request=request)
                return redirect(reverse('main'))
            else:
                login_form.add_error(None, "Invalid username or password")
                return render(request, 'user_login.html', {
                  'form':login_form
                })

    else:
        login_form = UserLoginForm()
        return render(request, 'user_login.html', {
            'form':login_form
        })
def register(request):
    User = get_user_model()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # check if the username and password matches
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                # actually log the user in
                auth.login(user=user, request=request)
                messages.success(request, "You have registered successful")
            else:
                messages.error(request, "You failed to register")
            return redirect(reverse('index'))
        else:
            return render(request, "register.html",{
                'form': form
            })
    else:
        register_form = UserRegistrationForm()
        return render(request, "register.html", {
            'form': register_form
        })
        
