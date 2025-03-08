from django.urls import path
from .import views

app_name = 'companies'


urlpatterns = [     
    # API REST
    path('', views.getAllCompanies,name='list_companies'),
    path('create/', views.createCompany, name='create_company'),
    path('create_company_form/<int:user_id>/', views.create_company_form, name='create_company_form'),
    path('<int:id>/detail/', views.companyDetail, name='detail'),
    path('<int:id>/update/', views.companyDetail, name='update_company_or'),
    path('<int:id>/delete/', views.companyDetail, name='delete_company'),

    # VISTAS HTML
    path('<int:id>/cp-dashboard/', views.company_dashboard, name='company_dashboard'),
    path('<int:id>/cp-update/', views.update_company, name='update_company'),
]
