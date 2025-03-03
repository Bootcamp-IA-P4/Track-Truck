from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.db import models

from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, user_type='regular', **extra_fields):
        if not email:
            raise ValueError('El correo electrónico es obligatorio')
        if not username:
            raise ValueError('El nombre de usuario es obligatorio')

        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            user_type=user_type,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'users'
    COMPANY = 'company'
    DRIVER = 'driver'
    ADMIN = 'admin'

    USER_TYPE_CHOICES = [
        (COMPANY, 'Company'),
        (DRIVER, 'Driver'),
        (ADMIN, 'Admin')
    ]

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Django maneja el hash internamente
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default=DRIVER)
    created_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'  # Usa 'username' si prefieres autenticación por nombre de usuario
    REQUIRED_FIELDS = ['username', 'user_type']

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Add this line
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Add this line
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"

