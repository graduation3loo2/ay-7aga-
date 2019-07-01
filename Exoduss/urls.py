from django.contrib import admin
from django.urls import path, include
from singup import views as user_views
from rest_framework import routers
from api.views import *


router = routers.DefaultRouter()
router.register(r'trips', TripsViewSet, "trips")
router.register(r'votes', VotesViewSet, "response")
router.register(r'recent', RecentViewSet, "recent")
router.register(r'users', UserListViewSet, "users")
router.register(r'follow', FollowViewSet, "follow")
router.register(r'home_trips', TripsHomeViewSet, "home_trips")
router.register(r'home_agencies', AgenciesHomeViewSet, "home_agencies")
router.register(r'interests', InterestsModelViewSet, 'interests')

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
    path('api/user/<int:pk>/', UserView.as_view()),
    path('api/userpass/<int:pk>/', UserPasswordView.as_view()),
    path('api/user/login/', UserLoginView.as_view()),
    path('api/interests/<int:pk>', InterestedVoteViewSet.as_view()),
    path('api/trips/<int:pk>', TripView.as_view()),
    path('api/users/<int:pk>', OneUserView.as_view()),
    path('api/', include(router.urls)),
]