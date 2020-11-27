from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from . models import *
def list_hotels(request) :

    # all_hotels = "<ul>"

    # for hotel in Hotel.objects.all() :
    #     all_hotels = all_hotels + "<li>" + hotel.hotel_name + "</li>"
    # all_hotels += "</ul>"
    hotels = Hotel.objects.all() 
    context = {
        'hotels':hotels
    }

    return render(request,'reservation/index.html',context)
