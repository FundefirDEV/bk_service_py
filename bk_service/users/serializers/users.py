""" Users serializers """

# Django
from django.core.validators import RegexValidator
from django.contrib.auth import password_validation

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from bk_service.users.models import User  # , Profile


# Simple JWT
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserLoginSerializer(serializers.Serializer):
    """ User login serializers 
    Handle the login request data"""

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)


class UserSignUpSerializer(serializers.ModelSerializer):
    """ User SignUp serializers 
    Handle the SignUp request data"""

    password = serializers.CharField(min_length=8, max_length=128, required=True)
    password_confirmation = serializers.CharField(min_length=8, max_length=128, required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'gender', 'first_name',
                  'last_name', 'phone_number', 'city', 'password', 'password_confirmation']

    def create(self, validated_data, *args, **kwargs):

        user = User.objects.create_user(**validated_data)

        return user

    def validate(self, data):

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise serializers.ValidationError("Password don't match")

        try:
            password_validation.validate_password(password)

        except:
            raise serializers.ValidationError("This password is too common")

        return data


class UserModelSerializer(serializers.ModelSerializer):
    """ User model serializers """
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'gender', 'first_name',
                  'last_name', 'phone_number', 'city', 'is_verified')

        # extra_kwargs = {'first_name': {'required': True, 'allow_blank': False}}
        # extra_kwargs = {'last_name': {'required': True, 'allow_blank': False}}
        # extra_kwargs = {'phone_number': {'required': True, 'allow_blank': False}}
        # extra_kwargs = {'password': {'required': True, 'allow_blank': False}}

    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data, is_verified=False)
    #     profile = Profile.objects.create(user=user)
    #     return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        # The default result (access/refresh tokens)
        token_data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        # Custom token_data you want to include
        user_serializer = UserModelSerializer(self.user)

        token_data['access_token'] = token_data.pop('access')
        token_data['refresh_token'] = token_data.pop('refresh')

        data = {**token_data, **user_serializer.data}

        # import pdb
        # pdb.set_trace()

        return data
