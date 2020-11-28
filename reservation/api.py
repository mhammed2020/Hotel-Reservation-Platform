from rest_framework.viewsets import ModelViewSet

from . serializers import HotelSerializer
from . models import Hotel


class HotelAPI(ModelViewSet) :
    queryset = Hotel.objects.all() #get all Hotel model
    serializer_class = HotelSerializer