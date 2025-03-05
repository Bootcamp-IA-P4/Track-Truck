from django.urls import path
from .views import get_all_drivers, create_driver, driver_detail, create_driver_form

app_name = "drivers"

urlpatterns = [
    path("", get_all_drivers, name="get_all_drivers"),
    path("create/", create_driver, name="create_driver"),
    path("<int:id>/detail/", driver_detail, name="driver_detail"),
    path ("<int:id>/update/", driver_detail, name="driver_detail"),
    path ("<int:id>/delete/", driver_detail, name="driver_detail"),
    path('create_driver_form/<int:user_id>/', create_driver_form, name='create_driver_form'),
]
