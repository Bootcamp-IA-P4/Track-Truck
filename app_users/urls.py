from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.signin),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view),
]
