from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tour(models.Model):
    package_name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    images = models.ImageField(upload_to='product_image')
    price = models.IntegerField()
    options ={
        ('adventure trip','Adventure Trips'),
        ('family trip','Family Trips'),
        ('cultural trip','Cultural Trips'),
        ('beach vacation','Beach Vacations'),
        ('cruise trip','Cruise trips')
    }

    category = models.CharField(max_length=100,choices=options)

class Popular(models.Model):
    card_title = models.CharField(max_length=150)
    card_description = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    images = models.ImageField(upload_to='popular_image')
    price = models.IntegerField()
    options ={
        ('popular','popular'),
    }

    category = models.CharField(max_length=100,choices=options)

class WishList(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    package = models.ForeignKey(Tour,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class Booking(models.Model):
    package = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    num_people = models.IntegerField()
    phone = models.IntegerField()
    address = models.CharField(max_length=300)
