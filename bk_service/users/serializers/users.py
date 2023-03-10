""" Users serializers """

# Django
from django.core.validators import RegexValidator
from django.contrib.auth import password_validation

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from bk_service.users.models import User
from bk_service.locations.models import City
from bk_service.banks.models import PartnerGuest, Partner, PartnerDetail

# Serializers
from bk_service.locations.serializers import CityModelSerializer
# Simple JWT
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Utils
from bk_service.utils.enums.banks import PartnerType
from bk_service.utils.exceptions_errors import CustomException
from bk_service.utils.constants_errors import *


class PhoneExistSerializer(serializers.Serializer):

    phone_number = serializers.CharField(

        required=True,

        validators=[
            UniqueValidator(queryset=User.objects.all(), message=build_error_message(PHONE_EXIST))
        ],
        error_messages={
            'required': build_error_message(PHONE_REQUIRED),
            'invalid': build_error_message(PHONE_INVALID),
        },
    )


class EmailExistSerializer(serializers.Serializer):

    email = serializers.EmailField(

        required=True,

        validators=[
            UniqueValidator(queryset=User.objects.all(), message=build_error_message(EMAIL_EXIST))
        ],
        error_messages={
            'required': build_error_message(EMAIL_REQUIRED),
            'invalid': build_error_message(EMAIL_INVALID),
        },
    )


class UserLoginSerializer(serializers.Serializer):
    """ User login serializers
    Handle the login request data"""

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)


class UserSignUpSerializer(serializers.ModelSerializer):
    """ User SignUp serializers
    Handle the SignUp request data"""

    password = serializers.CharField(
        min_length=8,
        max_length=128,
        required=True,
        error_messages={
            'required': build_error_message(PASSWORD_REQUIRED),
            'invalid': build_error_message(PASSWORD_INVALID),
        },
    )
    password_confirmation = serializers.CharField(
        min_length=8,
        max_length=128,
        required=True,
        error_messages={
            'required': build_error_message(PASSWORD_CONFIRMATION_REQUIRED),
            'invalid': build_error_message(PASSWORD_CONFIRMATION_INVALID),
        },
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'gender', 'first_name',
                  'last_name', 'phone_number', 'phone_region_code', 'password', 'password_confirmation', 'city']
        extra_kwargs = {
            'email': {
                "error_messages": {
                    'required': build_error_message(EMAIL_REQUIRED),
                    'unique': build_error_message(EMAIL_EXIST),
                    'invalid': build_error_message(EMAIL_INVALID),
                }
            },
            'phone_number': {
                "error_messages": {
                    'required': build_error_message(PHONE_REQUIRED),
                    'unique': build_error_message(PHONE_EXIST),
                    'invalid': build_error_message(PHONE_INVALID),
                }
            },
            'username': {
                "error_messages": {
                    'required': build_error_message(USERNAME_REQUIRED),
                    'unique': build_error_message(USERNAME_EXIST),
                    'invalid': build_error_message(USERNAME_INVALID),
                },
            },
            'first_name': {
                "error_messages": {
                    'required': build_error_message(FIRST_NAME_REQUIRED),
                    'invalid': build_error_message(FIRST_NAME_INVALID),
                },
            },
            'last_name': {
                "error_messages": {
                    'required': build_error_message(LAST_NAME_REQUIRED),
                    'invalid': build_error_message(LAST_NAME_INVALID),
                },
            },
            'phone_region_code': {
                "error_messages": {
                    'required': build_error_message(PHONE_REGION_CODE_REQUIRED),
                    'invalid': build_error_message(PHONE_REGION_CODE_INVALID),
                }
            },
            # 'city': {
            #     "error_messages": {
            #         # 'required': build_error_message(CITY_REQUIRED),
            #         'invalid': build_error_message(CITY_INVALID),
            #         'does_not_exist': build_error_message(CITY_INVALID)
            #     }
            # },
            'gender': {
                "error_messages": {
                    'required': build_error_message(GENDER_REQUIRED),
                    'invalid': build_error_message(GENDER_INVALID),
                    'does_not_exist': build_error_message(GENDER_INVALID)
                }
            },
        }

    def create(self, validated_data, *args, **kwargs):

        user = User.objects.create_user(**validated_data)

        partner_guest = self.find_partner_guest(user)

        if partner_guest is not None:

            partner = Partner.objects.create(
                phone_number=partner_guest.phone_number,
                phone_region_code=partner_guest.phone_region_code,
                bank=partner_guest.bank,
                user=user,
                role=PartnerType.partner,
            )
            partner_guest.is_active = True
            partner_guest.save()

        return user

    def validate(self, data):

        # Validate Pass
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise CustomException(error=PASSWORD_CONFIRMATION)
        try:
            password_validation.validate_password(password)
        except:
            raise CustomException(error=PASSWORD_TOO_COMMON)

        return data

    def find_partner_guest(self, user):

        try:
            partner_guest = PartnerGuest.objects.get(
                phone_number=user.phone_number,
                phone_region_code=user.phone_region_code,
                is_active=False
            )

            return partner_guest
        except:
            return None


class UserModelSerializer(serializers.ModelSerializer):
    """ User model serializers """
    city = CityModelSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'gender', 'first_name',
                  'last_name', 'phone_number', 'city', 'is_verified', 'is_staff')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        # The default result (access/refresh tokens)
        token_data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        # Custom token_data you want to include
        user_serializer = UserModelSerializer(self.user)

        token_data['access_token'] = token_data.pop('access')
        token_data['refresh_token'] = token_data.pop('refresh')

        partner = self.user.get_partner()
        partner_data = {}

        if partner is not None:
            partner_data['partner_id'] = partner.id
            partner_data['role'] = partner.role

        data = {**token_data, **user_serializer.data, **partner_data}

        # # import pdb
        # pdb.set_trace()

        return data


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'gender', 'phone_region_code')
        extra_kwargs = {
            'username': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
            'phone_number': {'required': True},
            'gender': {'required': True},
            'phone_region_code': {'required': True},
        }

    def validate_email(self, user, email):
        if User.objects.exclude(pk=user.pk).filter(email=email).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})

    def validate_phone(self, user, phone_number, phone_region_code):
        if User.objects.exclude(pk=user.pk).filter(phone_number=phone_number, phone_region_code=phone_region_code).exists():
            raise serializers.ValidationError({"phone_number": "This phone number is already in use."})

    def validate_username(self, user, username):
        if User.objects.exclude(pk=user.pk).filter(username=username).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
