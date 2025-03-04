from django.db import models

# Create your models here.
class Shipment(models.Model):
    shipment_id = models.IntegerField(unique=True,null=False)
    company_id = models.IntegerField(unique=True,null=False)
    driver_id = models.IntegerField(unique=True,null=False)
    description = models.TextField()
    origin = models.TextField()
    destination = models.TextField()
    created_at = models.DateField()
    finished_at = models.DateField()

    class Meta:
        db_table = 'shipments'
    
    def __str__(self):
        return self.shipment_id+'-'+self.description

