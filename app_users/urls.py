from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.signin),
    path('login/', views.login),
    path('forgot_password/', views.forgot_password),
]
