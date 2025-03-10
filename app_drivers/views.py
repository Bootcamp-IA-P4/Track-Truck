from django.shortcuts import get_object_or_404, render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Driver
from .serializers import DriverSerializer
import requests
from datetime import datetime
import json
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Obtener todos los conductores
@api_view(['GET'])
def get_all_drivers(request):
    drivers = Driver.objects.all()
    serializer = DriverSerializer(drivers, many=True)
    return Response(serializer.data)

# Crear un nuevo conductor
@api_view(['POST'])
def create_driver(request):
    serializer = DriverSerializer(data=request.data)
    if Driver.objects.filter(truck_plate=request.data.get('truck_plate')).exists():
        return Response({"error": "A driver with this truck plate already exists."}, status=status.HTTP_400_BAD_REQUEST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Obtener, actualizar o eliminar un conductor por ID
@api_view(['GET', 'PUT', 'DELETE'])
def driver_detail(request, id):
    driver = get_object_or_404(Driver, pk=id)

    if request.method == 'GET':  # 🔹 Obtener un conductor específico
        serializer = DriverSerializer(driver)
        return Response(serializer.data)

    elif request.method == 'PUT':  # 🔹 Actualizar un conductor
        serializer = DriverSerializer(instance=driver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':  # 🔹 Eliminar un conductor
        driver.delete()
        return Response({"message": "Conductor eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)

def create_driver_form(request, user_id):
    if request.method == 'POST':
        driver_data = {
            'user': user_id,
            'name': request.POST.get('name'),
            'truck_plate': request.POST.get('truck_plate'),
            'phone': request.POST.get('phone')
        }
        response = requests.post('http://localhost:8000/drivers/create/', json=driver_data)
        
        if response.status_code == 201:
            driver_id = response.json().get('id')
            
            if driver_id:
                return redirect('drivers:driver_dashboard', id=driver_id)
            else:
                return redirect('home')
        else:
            try:
                error_message = response.json().get('error', 'Error creating driver')  # Extraer el mensaje de error de la respuesta JSON
            except:
                error_message = 'Error creating driver'

            return render(request, 'app_drivers/create_driver.html', {'error': error_message, 'user_id': user_id})
    else:
        return render(request, 'app_drivers/create_driver.html', {'user_id': user_id})

# VISTAS QUE LLAMAN A LA API Y DEVUELVEN HTMLS

@login_required(login_url='login')
def driver_dashboard(request, id):
    driver = get_object_or_404(Driver, id=id)
    
    # llamamos a la API para obtener los envíos del driver
    shipments_url = f"http://127.0.0.1:8000/shipments/{id}/dr-shipments/"
    response = requests.get(shipments_url)

    shipments = []
    if response.status_code == 200:
        shipments = response.json()  # convertimos la respuesta JSON en una lista de diccionarios

        # convertimos y formatear las fechas
        for shipment in shipments:
            shipment["created_at"] = datetime.fromisoformat(shipment["created_at"].replace("Z", "")).strftime("%Y-%m-%d %H:%M")
            shipment["finished_at"] = datetime.fromisoformat(shipment["finished_at"].replace("Z", "")).strftime("%Y-%m-%d %H:%M")
    return render(request, 'app_drivers/dr-dashboard.html', {
        'driver': driver,
        'shipments': shipments
    })

@login_required(login_url='login')
def update_driver(request, id):
    # URL para obtener los datos del conductor
    api_url = f"http://127.0.0.1:8000/drivers/{id}/detail/"
    response = requests.get(api_url)

    if response.status_code == 200:
        driver = response.json()
    else:
        return render(request, "app_drivers/dr-update.html", {"error": "Error al obtener datos."})

    if request.method == "POST":
        # recogemos los datos del formulario
        data = {
            "name": request.POST["name"],
            "truck_plate": request.POST["truck_plate"],
            "phone": request.POST["phone"],
            "user": driver["user"]
        }

        # convertimos el diccionario en JSON
        json_data = json.dumps(data)
        headers = {'Content-Type': 'application/json'}

        # hacemos la solicitud PUT con los datos en formato JSON
        update_response = requests.put(api_url, data=json_data, headers=headers)

        if update_response.status_code == 200:
            return redirect(f"/drivers/{id}/dr-dashboard/")
        else:
            return render(request, "app_drivers/dr-update.html", {
                "driver": driver,
                "error": "Error al actualizar el conductor. Verifica los datos."
            })

    return render(request, "app_drivers/dr-update.html", {"driver": driver})