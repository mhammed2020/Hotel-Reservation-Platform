from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request) :

    return HttpResponse ("hello it s me .. django from reservation views ")
