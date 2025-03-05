from django.contrib import admin
from .models import User

# Register your models here.
#admin.site.register(User)

from django.urls import reverse
from django.shortcuts import redirect


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type', 'is_staff', 'is_superuser')
    list_filter = ('user_type', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')

    def add_view(self, request, form_url='', extra_context=None):
        # Redirige al formulario personalizado de creación de usuario
        return redirect(reverse('signin'))

    def response_add(self, request, obj, post_url_continue=None):
        # Redirige después de añadir un usuario
        return redirect(reverse('admin:app_users_user_changelist'))

    def has_add_permission(self, request):
        # Solo permite añadir usuarios a los superusuarios
        return request.user.is_superuser

