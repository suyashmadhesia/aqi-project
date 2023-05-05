from django.db import models

# Create your models here.

class AQI(models.Model):
    pm25 = models.FloatField()
    pm10 = models.FloatField()
    no = models.FloatField()
    no2 = models.FloatField()
    nox = models.FloatField()
    co = models.FloatField()
    temp= models.FloatField()