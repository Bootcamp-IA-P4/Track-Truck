from django.contrib.auth import login as auth_login, logout as auth_logout
import requests

from app_companies.forms import CompanyForm
from app_drivers.forms import DriverForm
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.core.exceptions import PermissionDenied

# def custom_permission_denied_view(request, exception):
#     return render(request, '403.html', status=403)

# def is_admin(user):
#     if not user.is_authenticated or not user.is_superuser:
#         raise PermissionDenied("Page reserved for admin.")
#     return True


# @user_passes_test(is_admin, login_url='login')
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect
from .forms import CustomUserCreationForm
import requests

def signin(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            if user.user_type == 'company':
                return redirect('companies:create_company_form', user_id=user.id)
            elif user.user_type == 'driver':
                    return redirect('drivers:create_driver_form', user_id=user.id)
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signin.html', {'form': form})





def login_view(request):
    if request.method == 'POST':


            auth_login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm
    return render(request, 'users/signin.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('login')


