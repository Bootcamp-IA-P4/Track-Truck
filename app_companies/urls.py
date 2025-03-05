from django.urls import path
from .import views

urlpatterns = [     
    # API REST
    path('', views.getAllCompanies),
    path('create/', views.createCompany),
    path('<int:id>/detail/', views.companyDetail),
    path('<int:id>/update/', views.companyDetail),
    path('<int:id>/delete/', views.companyDetail),

    # VISTAS HTML
    path('<int:id>/cp-dashboard/', views.company_dashboard, name='company_dashboard'),
    path('<int:id>/cp-update/', views.update_company, name='update_company'),
]