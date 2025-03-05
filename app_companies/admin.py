from django.contrib import admin
from .models import Company

# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'user_id')
    search_fields = ('name', 'email', 'user_id')
    list_filter = ('email', 'user_id')

