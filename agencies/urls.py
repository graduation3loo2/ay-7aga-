from django.urls import path
from . import views



urlpatterns=[

        path('', views.agencies, name='agencies'),

]