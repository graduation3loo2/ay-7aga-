from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='agency_main'),
    path('a', views.agencies, name='agencies'),
    path('a/', include('agency.urls')),
    path('follow', views.follow, name='follow'),
    path('unfollow', views.un_follow, name='unfollow'),
]
