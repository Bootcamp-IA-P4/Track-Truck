from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    user_id = models.ForeignKey('app_users.User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'companies'
        managed = False
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name