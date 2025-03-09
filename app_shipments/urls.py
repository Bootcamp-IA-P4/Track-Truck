from django.urls import path
from . import views

app_name = 'shipments'


urlpatterns = [

    #path('', views.shipmentList),
    path('<int:id>/co-shipments/', views.companyShipments),
    path('shipments-add/', views.shipmentCreate, name='create_shipment'),
    path('<int:id>/dr-shipments/', views.driverShipments),
    
    path('without_driver/', views.shipmentWithoutDriver, name='shipment_without_driver'),
    path('shipments-add-dashboard/', views.shipmentCreateDashboard, name='create_shipment_dashboard'),

    # Ruta para ver los shipments sin conductor
    path('shp-without-dr/', views.shipmentWithoutDriverPage, name='shipment_without_dr_page'),

    # Ruta para asignar un shipment a un conductor
    path('<int:id>/assign-driver/<int:driver_id>/', views.assignDriverToShipment, name='assign_driver_to_shipment'),

]