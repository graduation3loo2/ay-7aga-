from django.urls import path
from . import views

urlpatterns = [
        path('', views.trips_main, name='trips'),
        path('t', views.trips, name='Trips'),
        path('filter', views.trips_form, name='Trips_form'),
]
