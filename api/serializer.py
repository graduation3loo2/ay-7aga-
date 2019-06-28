from django.db.models import Q
from rest_framework import serializers

from cryptography.fernet import Fernet
import base64

from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, EmailField

from Exoduss import settings

from trips.models import Trips
from user.models import Follows, Users, GoingTo
from votes.models import Vote, Response


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


class ResponseSerializer(serializers.ModelSerializer):
    vote = VoteSerializer(many=False)

    class Meta:
        model = Response
        fields = "__all__"


class FollowsSerializer(serializers.ModelSerializer):
    agency_name = serializers.ReadOnlyField(source='agency.name')
    agency_rate = serializers.ReadOnlyField(source='agency.rate')
    agency_photo = serializers.ReadOnlyField(source='agency.photo_url')
    agency_bio = serializers.ReadOnlyField(source='agency.bio')

    class Meta:
        model = Follows
        fields = "__all__"


class FollownumberSerializer(serializers.ModelSerializer):

    number = Follows.objects.raw('select count(Exodus.Follows.user_id) from Exodus.Follows group by agency_id;')

    class Meta:
        model = Follows
        fields = ("agency_id", "number")


class GoingSerializer(serializers.ModelSerializer):

    number = GoingTo.objects.raw('select count(Exodus.going_to.User_id) from Exodus.going_to group by going_to.Trip_id;')

    class Meta:
        model = GoingTo
        fields = ("Trip_id", "number")


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        email = validated_data.pop('e_mail', None)
        if Users.objects.filter(e_mail=email).exists():
            return serializers.ValidationError("user already exists")
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
        email = data.get("e_mail", None)
        password = data["password"]
        if not email:
            raise ValidationError("Email is required for login")

        user = Users.objects.filter(Q(e_mail__exact=email)).distinct()
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

        return data


class UserUpdateSerializer(serializers.ModelSerializer):
    pass


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = 'user_id'

