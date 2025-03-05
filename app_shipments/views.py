from django.shortcuts import render
from .serializer import ShipmentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Shipment


@api_view(['POST']) #CREATE
def shipmentCreate(request):
    serializer = ShipmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET']) 
def shipmentList(request):
    try:
        shipments = Shipment.objects.all()
        serializer = ShipmentSerializer(shipments, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def companyShipments(request, id):
    try:
        # Filtrar los envíos por el company_id que coincide con el parámetro 'id'
        shipments = Shipment.objects.filter(company_id=id)
        
        # Verificar si se encontraron envíos
        if not shipments:
            return Response({"detail": "No shipments found for this company."}, status=status.HTTP_404_NOT_FOUND)
        
        # Serializar los datos de los envíos encontrados
        serializer = ShipmentSerializer(shipments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        # Capturar cualquier error que ocurra y devolver un mensaje de error
        return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def driverShipments(request, id):
    try:
        # Filtrar los envíos por el company_id que coincide con el parámetro 'id'
        shipments = Shipment.objects.filter(driver_id=id)
        
        # Verificar si se encontraron envíos
        if not shipments:
            return Response({"detail": "No shipments found for this company."}, status=status.HTTP_404_NOT_FOUND)
        
        # Serializar los datos de los envíos encontrados
        serializer = ShipmentSerializer(shipments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        # Capturar cualquier error que ocurra y devolver un mensaje de error
        return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def shipmentUpdate(request):
    serializer = ShipmentSerializer(Shipment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def shipmentDelete():
    try:
        Shipment.delete()
        return Response({"message": "Shipment deleted"},status=status.HTTP_200_OK)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)