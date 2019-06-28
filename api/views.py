from rest_framework import viewsets, generics

# Create your views here.
from rest_framework.generics import RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny

from api.serializer import *
from trips.models import Trips
from votes.models import Vote, Response
from user.models import Follows, Users, GoingTo


class TripsViewSet(viewsets.ModelViewSet):
    queryset = Trips.objects.all()
    serializer_class = TripsSerializer


class VotesViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follows.objects.all()
    serializer_class = FollowsSerializer


class FollownumberViewSet(viewsets.ViewSet):
     queryset = Follows.objects.all()
     serializer_class = FollownumberSerializer


class GoingViewSet(viewsets.ViewSet):

     queryset = GoingTo.objects.all()
     serializer_class = GoingSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class RecentViewSet(viewsets.ModelViewSet):
    queryset = Trips.objects.order_by('date_from').reverse()
    serializer_class = RecentSerializer


class UserLoginViewset(viewsets.ModelViewSet):
    queryset = Users.objects.values_list('e_mail', 'password').filter()
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer


class UserUpdateView(RetrieveAPIView):
    queryset = Users.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserUpdateSerializer


class UserDeleteView(viewsets.ModelViewSet):
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Users.objects.filter(user_id=self.kwargs['pk'])
    queryset = get_queryset()
    queryset.delete()
    serializer_class = UserDeleteSerializer
