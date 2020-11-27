from django.db import models

# Create your models here.

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_city = models.CharField(max_length=100)
    total_rooms = models.IntegerField()
    empty_rooms = models.IntegerField()

    def __str__(self):
        return self.hotel_name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    def __str__(self):
         return str(self.hotel) + " Reserved for " +str(self.customer) + " Customer "
