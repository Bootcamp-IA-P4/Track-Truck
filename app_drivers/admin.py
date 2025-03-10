from django.contrib import admin
from .models import Driver


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "truck_plate", "phone")
    search_fields = ("user", "name", "truck_plate", "phone")
    list_filter = ("user", "truck_plate")

    # 🔹 Habilitar la edición de estos campos desde la lista
    list_editable = ("name", "truck_plate", "phone")

    # 🔹 Definir los campos que se mostrarán en la vista de edición
    fields = ("user", "name", "truck_plate", "phone")
