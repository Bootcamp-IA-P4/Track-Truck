from django.urls import path
from .views import get_all_drivers, create_driver, driver_detail

urlpatterns = [
    path("", get_all_drivers, name="get_all_drivers"),
    path("create/", create_driver, name="create_driver"),
    path("<int:id>/detail/", driver_detail, name="driver_detail"),
    path ("<int:id>/update/", driver_detail, name="driver_detail"),
    path ("<int:id>/delete/", driver_detail, name="driver_detail"),
]
