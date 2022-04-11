""" User views. """

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework import generics

# Simple JWT
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from bk_service.users.models.users import User
from bk_service.banks.models import PartnerDetail
# Serializers
from bk_service.users.serializers import (
    MyTokenObtainPairSerializer,
    UserSignUpSerializer,
    UserModelSerializer,
    UpdateUserSerializer
)

# Locations Models
from bk_service.locations.models import City


class UserLoginAPIView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserSingUpAPIView(APIView):

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserSignUpSerializer(data=data)
        # serializer.validate(data=data)

        serializer.is_valid(raise_exception=True)
        validated_data = dict(serializer.validated_data)

        # Clear data
        validated_data.pop('password_confirmation')

        # Create new User
        user = serializer.create(validated_data=validated_data)

        # get tokens
        refresh_token = RefreshToken.for_user(user)
        access_token = AccessToken.for_user(user)

        res = {
            'refresh_token': str(refresh_token),
            'access_token': str(access_token),
            'id': user.id,
            'partner_id': None
        }

        partner = user.get_partner()

        if partner is not None:
            res['partner_id'] = partner.id

        # # import pdb
        # pdb.set_trace()

        return Response(res)


class UpdateProfileView(APIView):

    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        serializer = UpdateUserSerializer()
        serializer.validate_email(user=user, email=data['email'])
        serializer.validate_phone(
            user=user, phone_number=data['phone_number'],
            phone_region_code=data['phone_region_code']
        )
        serializer.validate_username(
            user=user,
            username=data['username']
        )
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.email = data['email']
        user.username = data['username']
        user.phone_number = data['phone_number']
        user.gender = data['gender']
        user.phone_region_code = data['phone_region_code']
        user.partner.phone_number = data['phone_number']
        user.partner.phone_region_code = data['phone_region_code']
        detail = PartnerDetail.objects.get(partner=user.partner)

        detail.document_number = data['document_number']
        detail.profession = data['profession']
        detail.scholarship = data['profession']
        detail.birth_date = data['birth_date']
        user.save()
        user.partner.save()
        detail.save()

        return Response('ok')

        # serializer.is_valid(raise_exception=True)
        # validated_data = dict(serializer.validated_data)
