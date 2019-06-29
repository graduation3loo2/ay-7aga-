from django.db.models import Count
from rest_framework import serializers, status

from cryptography.fernet import Fernet
import base64

from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, EmailField

from Exoduss import settings

from trips.models import Trips, TripPhotos, Agencies
from user.models import Follows, Users
from votes.models import Vote, Response as ResponseModel


class TripsSerializer(serializers.ModelSerializer):
    agency_name = serializers.ReadOnlyField(source='agency.name')

    class Meta:
        model = Trips
        fields = "__all__"


class VoteSerializer(serializers.ModelSerializer):
    agency_name = serializers.ReadOnlyField(source='agency.name')

    class Meta:
        model = Vote
        fields = "__all__"


class FollowsSerializer(serializers.ModelSerializer):
    agency_name = serializers.ReadOnlyField(source='agency.name')
    agency_rate = serializers.ReadOnlyField(source='agency.rate')
    agency_photo = serializers.ReadOnlyField(source='agency.photo_url')
    agency_bio = serializers.ReadOnlyField(source='agency.bio')

    class Meta:
        model = Follows
        fields = "__all__"


class UserListSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        email = validated_data['e_mail']
        if Users.objects.filter(e_mail=email).exists():
            return serializers.ValidationError("email already exists")
        password = validated_data.pop('password', None)
        cipher_suite = Fernet(settings.ENCRYPT_KEY)
        encrypted_text = cipher_suite.encrypt(password.encode('ascii'))
        encrypted_text64 = base64.urlsafe_b64encode(encrypted_text).decode("ascii")
        validated_data['password'] = encrypted_text64
        return Users.objects.create(**validated_data)

    class Meta:
        model = Users
        fields = (
            "__all__"
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }


class RecentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trips
        fields = "__all__"


class UserLoginSerializer(serializers.ModelSerializer):
    password = CharField(required=False, allow_blank=True)
    e_mail = EmailField(label="Email Adress", required=False, allow_blank=True)

    class Meta:
        model = Users
        fields = ['e_mail', 'password']
        extra_kwargs = {
            "password":    {
                "write_only": True
            }
        }

    def validate(self, data):
        email = data['e_mail']
        password = data["password"]
        if not email:
            raise ValidationError("Email is required for login")

        user = Users.objects.filter(e_mail__exact=email).distinct()
        user.exclude(e_mail__isnull=True).exclude(e_mail__iexact='')

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("Email is not valid")

        txt = base64.urlsafe_b64decode(user_obj.password)
        cipher_suite = Fernet(settings.ENCRYPT_KEY)
        decoded_text = cipher_suite.decrypt(txt).decode("ascii")

        if user_obj:
            if not password == decoded_text:
                raise ValidationError("Incorrect credentials")

        data["token"] = "SOME RANDOM TOKEN"
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class AgenciesHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agencies
        fields = ('agency_id', 'name', 'photo_url')


class TripsHomeSerializer(serializers.ModelSerializer):
    trip_name = serializers.ReadOnlyField(source='trip.name')

    class Meta:
        model = TripPhotos
        fields = ('trip', 'trip_name', 'url')


class InterestsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResponseModel
        fields = ('vote', 'interested', 'user')


class InterestedvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseModel
        fields = '__all__'


