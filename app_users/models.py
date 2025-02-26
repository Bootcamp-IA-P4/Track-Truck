from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    user_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    COMPANY = 'company'
    DRIVER = 'driver'

    USER_TYPE_CHOICES = [
        (COMPANY, 'Company'),
        (DRIVER, 'Driver'),
    ]

    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
    )


    class Meta:
        db_table = 'users'
        

    def __str__(self):
        return self.username + " " + self.user_type