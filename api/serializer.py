from rest_framework import serializers
from userauths.models import Profile, User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['full_name'] = user.full_name
        token['email'] = user.email
        token['username'] = user.username

        return token


class UserSerializer(serializers.ModelSerializer):
    """Doc"""
    class Meta:
        model = User
        field = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    """Doc"""
    class Meta:
        model = Profile
        field = '__all__'