# from django.shortcuts import render, redirect
# from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.shortcuts import render, redirect


def signin(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #login(request, user)
            auth_login(request, user)
            return redirect('home')
    else:
        #form = UserCreationForm()
        form = CustomUserCreationForm
    return render(request, 'users/signin.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        #form = AuthenticationForm(data=request.POST)
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            #login(request, user)
            auth_login(request, user)
            return redirect('home')
    else:
        #form = AuthenticationForm()
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    #logout(request)
    auth_logout(request)
    return redirect('login')


