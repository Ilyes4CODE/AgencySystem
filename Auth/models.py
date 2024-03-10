from django.db import models
from django.contrib.auth.models import User
from mainapp.models import Packages,Hotel,Rooms
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    pfp = models.ImageField(default="static/images/Default_pfp.jpg")
    passport_Number = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.user.username
    
class Reservation(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    package = models.ForeignKey(Packages, on_delete=models.CASCADE,null=True)
    date = models.DateField(auto_now_add=True,null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE,null=True)
    rooms = models.ForeignKey(Rooms, on_delete=models.CASCADE,null=True)
    is_accepted = models.BooleanField(default = False)
    def __str__(self):
        return self.user.user.username
     
