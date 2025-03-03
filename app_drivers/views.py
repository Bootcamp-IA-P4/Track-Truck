from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Driver
from .serializers import DriverSerializer

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
