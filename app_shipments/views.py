from django.shortcuts import render, redirect, get_object_or_404
from .serializer import ShipmentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Shipment
from django.contrib.auth.decorators import login_required


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


@login_required(login_url='login')
@api_view(['DELETE'])
def shipmentDelete():
    try:
        Shipment.delete()
        return Response({"message": "Shipment deleted"},status=status.HTTP_200_OK)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# VISTA PARA CREAR SHIPMENT DESDE DASHBOARD
@login_required(login_url='login')
@api_view(['POST']) 
def shipmentCreateDashboard(request):
    try:
        data = request.data.copy()

        last_shipment = Shipment.objects.order_by('-id').first()
        data['id'] = last_shipment.id + 1 if last_shipment else 1

        if 'finished_at' in data and data['finished_at'] == '':
            data.pop('finished_at')

        company_id = data.get('company_id')

        serializer = ShipmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            if company_id:
                return redirect('companies:company_dashboard', id=company_id)
            else:
                return Response({"error": "No company ID provided"}, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# VISTA API PARA SHIPMENTS SIN DRIVER_ID
@api_view(['GET'])
def shipmentWithoutDriver(request):
    try:
        shipments = Shipment.objects.filter(driver_id__isnull=True)
        
        if not shipments:
            return Response({"detail": "No shipments without driver found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ShipmentSerializer(shipments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# VISTA PARA ASIGNAR UN DRIVER A UN SHIPMENT
@login_required(login_url='login')
def shipmentWithoutDriverPage(request):
    shipments = Shipment.objects.filter(driver_id__isnull=True)

    driver = None
    if hasattr(request.user, 'driver') and request.user.driver:
        driver = request.user.driver

    return render(request, 'shipments/shipment_without_driver_list.html', {
        'shipments': shipments,
        'driver': driver
    })


@login_required(login_url='login')
def assign_driver_to_shipment(request, shipment_id):
    try:
        driver = request.user.driver
    except AttributeError:
        return redirect('some_error_page')
    shipment = get_object_or_404(Shipment, id=shipment_id)

    if shipment.driver_id is not None:
        return redirect('shipments:shipment_without_driver')
    
    shipment.driver_id = driver.id
    shipment.save()

    return redirect('drivers:driver_dashboard', id=driver.id)


@login_required(login_url='login')
@api_view(['POST'])
def shipmentDelete(request, id):
    shipment = get_object_or_404(Shipment, id=id)

    if shipment.driver_id is None:  # Solo permitir eliminar si no tiene driver
        shipment.delete()
        return redirect('companies:company_dashboard', id=shipment.company_id)

    return Response({"error": "Cannot delete a shipment with a driver assigned."}, status=status.HTTP_400_BAD_REQUEST)
