from django.db import models
from app_users.models import User

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100,null=True,blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='companies', db_column='user_id')


    class Meta:
        db_table = 'companies'
        #managed = False
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


{
  "name": "CompanyByApp",
  "email": "aa@app.com",
  "phone": "123456",
  "address": "123, abc, xyz",
  "user_id": 11
}
