""" User views. """

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


# Simple JWT
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

# Serializers
from bk_service.users.serializers import (
    MyTokenObtainPairSerializer,
    UserSignUpSerializer,
    UserModelSerializer
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

        # import pdb
        # pdb.set_trace()

        return Response(res)
