from django.urls import path
from .import views

urlpatterns = [     
    path('', views.getAllCompanies),
    path('create/', views.createCompany),
    path('<int:id>/detail/', views.companyDetail),
    path('<int:id>/update/', views.companyDetail),
    path('<int:id>/delete/', views.companyDetail),
]