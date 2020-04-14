from django.db import models
from driver.models import *
# Create your models here.
class userCoordinates(models.Model):
    location= models.CharField(max_length=100)
    phone= models.CharField(max_length=100)
    pick_status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.location


class Hospital(models.Model):
    hname= models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    h_loc = models.CharField(max_length=100)
    h_mobile = models.CharField(max_length=100)

    def __str__(self):
        return self.hname + ', ' + self.area