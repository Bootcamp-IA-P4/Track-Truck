from django.urls import path
from .import views

app_name = 'drivers'
urlpatterns = [
    path("", views.get_all_drivers, name="get_all_drivers"),
    path("create/", views.create_driver, name="create_driver"),
    path("<int:id>/detail/", views.driver_detail, name="driver_detail"),
    path("<int:id>/update/", views.driver_detail, name="driver_detail"),
    path("<int:id>/delete/", views.driver_detail, name="driver_detail"),
    path('create_driver_form/<int:user_id>/', views.create_driver_form, name='create_driver_form'),

    # VISTAS HTML
    path('<int:id>/dr-dashboard/', views.driver_dashboard, name='driver_dashboard'),
    path('<int:id>/dr-update/', views.update_driver, name='update_driver'),
]
