from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
