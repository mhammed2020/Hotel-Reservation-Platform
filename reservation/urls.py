from django.urls import path
from . import views
from . import api
from django.conf.urls import url

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("hotelsapi",api.HotelAPI)
urlpatterns = router.urls
urlpatterns += [

        path('hotels', views.list_hotels),
                # path('hotelsapi', api.HotelAPI.as_view()),

        path('customers', views.list_customers),
                path('', views.list_reservation)


]
