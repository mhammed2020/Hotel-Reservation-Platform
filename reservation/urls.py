from django.urls import path
from . import views
from . import api
urlpatterns = [
        # path('hotels', views.list_hotels),
                path('hotels', api.HotelAPI.as_view()),

        path('customers', views.list_customers),
                path('', views.list_reservation)


]
