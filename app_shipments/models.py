from django.db import models

# Create your models here.
class Shipment(models.Model):
    id = models.IntegerField(unique=True,null=False,primary_key=True)
    company_id = models.IntegerField(unique=True,null=False)
    driver_id = models.IntegerField(unique=True,null=False)
    description = models.TextField()
    origin = models.TextField()
    destination = models.TextField()
    created_at = models.DateTimeField()
    finished_at = models.DateTimeField()

    class Meta:
        db_table = 'shipments'
    
    def __str__(self):
        return(f'{self.id}-{self.description}')