from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import MyUser
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .forms import UserLoginForm, UserRegistrationForm, UpdateDetailsForm
from django.template.context_processors import csrf

def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index')) # go back to home page


def login(request):
    # Returns the login page
    if request.method == 'POST':
        # populate the form from what the user has keyed in
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            # attempt to check the username and password is valid
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            # different messages whether correct login details are entered or not
            if user:
                # log in the user
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in")
                return redirect(reverse('products'))
            else:
                messages.error(request, "Invalid login")
                return render(request, 'user_login.html', {
                    'form': login_form
                })

    else:
        login_form = UserLoginForm()
        return render(request, 'user_login.html', {
            'form': login_form
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
                messages.success(request, "You have registered successfully")
            else:
                messages.error(request, "You failed to register")
            return redirect(reverse('index'))
        else:
            return render(request, "register.html", {
                'form': form
            })
    else:
        register_form = UserRegistrationForm()
        return render(request, "register.html", {
            'form': register_form
        })


@login_required
def update_details(request):
    logged_in_user = MyUser.objects.all().get(pk=request.user.id)
# get data from the update details form
    if request.method == "POST":
        # for update
        update_details_form = UpdateDetailsForm(
            request.POST, instance=logged_in_user)
        if update_details_form.is_valid():
            update_details_form.save()
            messages.success(
                request, "Your profile has been updated! Please log in again")

    else:
        update_details_form = UpdateDetailsForm(instance=logged_in_user)

    return render(request, 'update_details.html', {
        'update_details_form': update_details_form
    })
