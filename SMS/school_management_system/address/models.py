from django.db import models

# Create your models here.
class PresentAddress(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street_address = models.CharField(max_length=100)

class PermanentAddress(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street_address = models.CharField(max_length=100)
    