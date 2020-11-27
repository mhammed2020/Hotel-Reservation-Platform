from django.urls import path
from . import views
urlpatterns = [
        path('hotels', views.list_hotels),
        path('customers', views.list_customers),
                path('', views.list_reservation)


]
