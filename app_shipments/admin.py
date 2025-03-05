from django.contrib import admin
from .models import Shipment

@admin.register(Shipment)

class BookAdmin(admin.ModelAdmin):
    list_display = ('description', 'origin', 'destination', 'driver_id', 'company_id', 'created_at', 'finished_at' )

    search_fields = ('id','description', 'origin', 'destination', 'driver_id', 'company_id', 'created_at', 'finished_at' )

    list_filter = ('driver_id','company_id')