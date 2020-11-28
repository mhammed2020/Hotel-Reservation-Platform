from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from . models import *
def list_hotels(request) :
    hotels = Hotel.objects.all() 
    context = {
        'hotels':hotels
    }

    return render(request,'reservation/hotels.html')


def list_customers(request) :

    customers = Customer.objects.all() 
    context = {
        'customers':customers
    }

    return render(request,'reservation/customers.html',context)


def list_reservation(request) :
    
    reservations = Reservation.objects.all() 
    context = {
        'reservations':reservations
    }

    return render(request,'reservation/reservations.html',context)