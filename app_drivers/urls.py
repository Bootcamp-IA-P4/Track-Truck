from django.urls import path
from .views import get_all_drivers, create_driver, driver_detail

urlpatterns = [
    path('drivers/', get_all_drivers, name="get_all_drivers"),
    path('drivers/create/', create_driver, name="create_driver"),
    path('drivers/<int:id>/', driver_detail, name="driver_detail"),
]
