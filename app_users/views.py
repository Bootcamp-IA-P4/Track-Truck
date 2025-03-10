from django.contrib.auth import login as auth_login, logout as auth_logout
import requests

from app_companies.forms import CompanyForm
from app_drivers.forms import DriverForm
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required

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
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)

            if user.user_type == 'company':
                company = user.companies.first()
                return redirect('companies:company_dashboard', id=company.id)
            elif user.user_type == 'driver':
                driver = user.driver
                return redirect('drivers:driver_dashboard', id=driver.id)
            else:
                return redirect('login')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('login')
