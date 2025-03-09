from django.urls import path
from . import views

app_name = 'shipments'


urlpatterns = [

    #path('', views.shipmentList),
    path('<int:id>/co-shipments/', views.companyShipments),
    path('shipments-add/', views.shipmentCreate, name='create_shipment'),
    path('<int:id>/dr-shipments/', views.driverShipments),
    


]