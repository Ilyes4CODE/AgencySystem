from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class Hotel && class Rooms
class Rooms(models.Model):
    room = models.CharField(max_length=50)
    def __str__(self):
        return self.room
    
class Hotel(models.Model):
    hotel_name = models.CharField(max_length=50)    
    def __str__(self):
        return self.hotel_name
    


class Packages(models.Model):
    image = models.ImageField(upload_to="images/upload/")
    Description = models.CharField(max_length=120)
    price = models.IntegerField(null=True)
    def __str__(self):
        return self.Description
    

