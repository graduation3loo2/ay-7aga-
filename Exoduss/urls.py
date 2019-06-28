from django.contrib import admin
from django.urls import path, include
from singup import views as user_views
from rest_framework import routers
from api.views import *


router = routers.DefaultRouter()
router.register(r'trips', TripsViewSet)
router.register(r'responses', ResponseViewSet)
router.register(r'recent', RecentViewSet)
router.register(r'users', UserViewSet)
router.register(r'follownumber', FollownumberViewSet)
router.register(r'follows', FollowViewSet)
router.register(r'login', UserLoginViewset)
router.register(r'goingto', GoingViewSet)
router.register(r'delete', UserDeleteView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('agencies/', include('agencies.urls')),
    path('', include('home.urls')),
    path('trips/', include('trips.urls')),
    path('votes/', include('votes.urls')),
    path('register/', user_views.register, name='register'),
    path('forms/', include('singup.urls')),
    path('user/', include('user.urls')),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
]