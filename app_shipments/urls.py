from django.urls import path
from . import views

urlpatterns = [

    #path('', views.shipmentList),
    path('<int:id>/companyshipments/', views.companyShipments),
    path('<int:id>/drivershipments/', views.driverShipments),
    


]