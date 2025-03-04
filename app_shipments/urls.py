from django.urls import path
from . import views

urlpatterns = [

    #path('', views.shipmentList),
    path('<int:id>/co-shipments/', views.companyShipments),
    path('<int:id>/dr-shipments/', views.driverShipments),
    


]