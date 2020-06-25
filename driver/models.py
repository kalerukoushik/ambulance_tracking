from django.db import models

# Create your models here.
class Driver(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    mobile = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, null=True)
    aadhar_no= models.CharField(max_length=15, null=True)
    driving_license_no = models.CharField(max_length=30, null=True)
    address = models.TextField(null=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'pics')
    def __str__(self):
        return self.username + ', ' + str(self.mobile)

class Ambulance(models.Model):
    # ambulance_location = models.CharField(max_length=100)
    driver_assigned = models.ForeignKey(Driver, on_delete=models.CASCADE)
    registration_no = models.CharField(max_length=50)
    engine_no = models.CharField(max_length=50, null=True)
    chasis_no = models.CharField(max_length=50, null=True)

    Front_view = models.ImageField(upload_to = 'pics', null=True)
    Side_view_1 = models.ImageField(upload_to = 'pics', null=True)
    Side_view_2 = models.ImageField(upload_to = 'pics', null=True)
    Back_view = models.ImageField(upload_to = 'pics', null=True)

    def __str__(self):
        return self.registration_no + ', ' + str(self.driver_assigned)
    