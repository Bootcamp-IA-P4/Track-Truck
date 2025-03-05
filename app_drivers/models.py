from django.db import models
from app_users.models import User  # Importamos el modelo User para relacionarlo

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación 1:1 con User
    name = models.CharField(max_length=255)
    truck_plate = models.CharField(max_length=50, unique=True)  # Matrícula del camión (única)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.truck_plate})"
    
    class Meta:
        db_table = 'drivers'
