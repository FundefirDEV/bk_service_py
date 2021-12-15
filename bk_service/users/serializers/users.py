""" Users serializers """

# Django REST Framework
from rest_framework import serializers

# Models
from bk_service.users.models import User, Profile

# Simple JWT
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserLoginSerializer(serializers.Serializer):
    """ User login serializers 
    Handle the login request data"""

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)


class UserModelSerializer(serializers.ModelSerializer):
    """ User model serializers """
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'gender', 'first_name',
                  'last_name', 'phone_number', 'is_client', 'is_verified')
        # fields = '__all__'
        extra_kwargs = {'first_name': {'required': True, 'allow_blank': False}}
        extra_kwargs = {'last_name': {'required': True, 'allow_blank': False}}
        extra_kwargs = {'phone_number': {'required': True, 'allow_blank': False}}
        extra_kwargs = {'password': {'required': True, 'allow_blank': False}}

    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data, is_verified=False)
    #     profile = Profile.objects.create(user=user)
    #     return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include
        user_serializer = UserModelSerializer(self.user)

        # import pdb; pdb.set_trace()

        data.update({'user': user_serializer.data})
        return data
