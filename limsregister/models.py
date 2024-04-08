from django.db import models

# Create your models here.
class FarmRegister(models.Model):
    farm_id = models.CharField(max_length=11,primary_key=True)
    farm_name = models.CharField(max_length=500)
    size = models.DecimalField(max_digits=5, decimal_places=2)
    unit_of_measure = models.CharField(max_length=50)
    size_in_hectares = models.DecimalField(max_digits=5, decimal_places=2)
    ownership = models.CharField(max_length=250)
    owner_name = models.CharField( max_length=250)
    company_name = models.CharField(max_length=250)
    nationality = models.CharField( max_length=50)
    gazette_status= models.CharField(max_length=50)
    diagram_no = models.CharField(max_length=50)
    title_type = models.CharField( max_length=50)
    deed_no = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    previous_district = models.CharField(max_length=70)
    current_district = models.CharField(max_length=50)
    farm_activity = models.CharField(max_length=50)
    remarks = models.CharField( max_length=500)

    def __str__(self):
        return self.farm_name
    