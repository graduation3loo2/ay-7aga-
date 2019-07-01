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
    queryset = TripPhotos.objects.all()
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
            password = data['password']
            user = Users.objects.filter(e_mail__icontains=data['e_mail']).first()
            txt = base64.urlsafe_b64decode(user.password)
            cipher_suite = Fernet(settings.ENCRYPT_KEY)
            decoded_text = cipher_suite.decrypt(txt).decode("ascii")
            if password == decoded_text:
                return JsonResponse({'message': "logged hhhhhhh", 'valid': True ,'user': {
                    'id': user.user_id,
                    'name': user.name,
                    'phone': user.phone,
                    'city': user.city,
                    'e_mail': user.e_mail,
                    'photo_url': user.photo_url
                }})
        return JsonResponse({'message': "Error credentials", 'valid': False})


class UserView(APIView):
    query_set = Users.objects.all()
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Users.objects.filter(user_id=pk).first()
        except Users.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    def patch(self, request, pk, format=None):
        user = self.get_object(pk)
        data = request.data
        serializer = UserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            if serializer.validated_data['name'] != '':
                user.name = serializer.validated_data['name']
            if serializer.validated_data['phone'] != '':
                user.phone = serializer.validated_data['phone']
            if serializer.validated_data['city'] != '':
                user.city = serializer.validated_data['city']
            if serializer.validated_data['e_mail'] != '':
                user.e_mail = serializer.validated_data['e_mail']
            serializer.save()
            return JsonResponse({'valid': True, 'user': {
                'name': user.name,
                'phone': user.phone,
                'city': user.city,
                'e_mail': user.e_mail,
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




class UserPasswordView(APIView):
    query_set = Users.objects.all()
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Users.objects.filter(user_id=pk).first()
        except Users.DoesNotExist:
            raise JsonResponse({"message": "user doesn't exist"})

    def patch(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserPassSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            password = serializer.validated_data['password']
            if password is not None and password != '':
                txt = base64.urlsafe_b64decode(user.password)
                cipher_suite = Fernet(settings.ENCRYPT_KEY)
                decoded_text = cipher_suite.decrypt(txt).decode("ascii")
            password_new = serializer.validated_data['password_new']
            if decoded_text == password and password_new is not None and password_new != '':
                cipher_suite = Fernet(settings.ENCRYPT_KEY)
                encrypted_text = cipher_suite.encrypt(password_new.encode('ascii'))
                encrypted_text64 = base64.urlsafe_b64encode(encrypted_text).decode("ascii")
                user.password = encrypted_text64
                serializer.save()
                return JsonResponse({'valid': True, "message": "password changed"})
            return JsonResponse({'message': "Error"})


class TripView(APIView):
    query_set = Trips.objects.all()
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Trips.objects.filter(trip_id=pk).first()
        except Users.DoesNotExist:
            raise JsonResponse({"message": "Trip doesn't exist"})

    def get(self, request, pk, format=None):
        trip = self.get_object(pk)
        serializer = TripSerializer(trip)
        return JsonResponse(serializer.data)


class OneUserView(APIView):
    query_set = Trips.objects.all()
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Users.objects.filter(user_id=pk).first()
        except Users.DoesNotExist:
            raise JsonResponse({"message": "Trip doesn't exist"})

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = OneUserSerializer(user)
        return JsonResponse(serializer.data)
