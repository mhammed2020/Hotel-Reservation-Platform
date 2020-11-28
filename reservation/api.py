from rest_framework.generics import ListAPIView
from . serializers import HotelSerializer
from . models import Hotel


class HotelAPI(ListAPIView) :
    queryset = Hotel.objects.all() #get all Hotel model
    serializer_class = HotelSerializer