from django.contrib import admin
from .models import Driver

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'truck_plate', 'phone')
    search_fields = ('user', 'name', 'truck_plate', 'phone')
    list_filter = ('user', 'truck_plate')

# Register your models here.
