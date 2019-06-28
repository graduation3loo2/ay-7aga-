from django.urls import path
from . import views


urlpatterns = [
    path('<str:agency_name>', views.agency, name='agency'),
    path('vote', views.agency_votes, name='agency_votes'),
]
