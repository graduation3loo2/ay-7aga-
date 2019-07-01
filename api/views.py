from django.http import Http404, JsonResponse
from rest_framework import viewsets

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from api.serializer import *
from trips.models import Trips
from votes.models import Vote, Response as ResponseModel
from rest_framework.response import Response as ResponseRest
from user.models import Follows, Users, GoingTo


class TripsViewSet(viewsets.ModelViewSet):
    queryset = Trips.objects.all()
    serializer_class = TripsSerializer


class VotesViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follows.objects.all()
    serializer_class = FollowsSerializer


class UserListViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserListSerializer


class RecentViewSet(viewsets.ModelViewSet):
    queryset = Trips.objects.order_by('date_from').reverse()
    serializer_class = RecentSerializer


class UserLoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer_class = UserLoginSerializer(data=data)

        if serializer_class.is_valid(raise_exception=True):
            user = Users.objects.filter(e_mail__icontains=data['e_mail'])
            return JsonResponse({'message': "logged hhhhhhh", 'valid': True ,'user': {
                'id': user[0].user_id,
                'name': user[0].name,
                'phone': user[0].phone,
                'city': user[0].city,
                'e_mail': user[0].e_mail
            }})
        return JsonResponse({'message': "Error credentials", 'valid': False})


class UserView(APIView):
    query_set = Users.objects.all()
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Users.objects.get(user_id=pk)
        except Users.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    def patch(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            password = serializer.validated_data['password']
            if serializer.validated_data['password'] is not None:
                if password is not None or password != '':
                    cipher_suite = Fernet(settings.ENCRYPT_KEY)
                    encrypted_text = cipher_suite.encrypt(password.encode('ascii'))
                    encrypted_text64 = base64.urlsafe_b64encode(encrypted_text).decode("ascii")
                    serializer.validated_data['password'] = encrypted_text64
                serializer.save()
            users = Users.objects.filter(user_id=pk)[0]
            return JsonResponse({'valid': True, 'user': {
                'name': users.name,
                'phone': users.phone,
                'city': users.city,
                'e_mail': users.e_mail,
            }})
        return JsonResponse({'message': "Error"})


    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return ResponseRest(status=status.HTTP_204_NO_CONTENT)


class AgenciesHomeViewSet(viewsets.ModelViewSet):
    serializer_class = AgenciesHomeSerializer
    queryset = Agencies.objects.all()


class TripsHomeViewSet(viewsets.ModelViewSet):
    serializer_class = TripsHomeSerializer
    queryset = TripPhotos.objects.all()


class InterestsModelViewSet(viewsets.ModelViewSet):
    serializer_class = InterestsSerializer
    queryset = ResponseModel.objects.all()


class InterestedVoteViewSet(APIView):
    serializer_class = InterestedvoteSerializer()
    permission_classes = [AllowAny]

    def get(self):
        query_set = ResponseModel.objects.filter(interested=1, vote_id=self.kwargs['pk']).count()
        return query_set
