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
from bk_service.banks.models import Partner


class UserLoginAPIView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserSingUpAPIView(APIView):

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserSignUpSerializer(data=data)
        serializer.validate(data=data)
        serializer.is_valid(raise_exception=True)

        # Clear data
        data.pop('password_confirmation')

        # get City
        city_id = data['city']
        data['city'] = City.objects.get(pk=city_id)

        # Create new User
        user = serializer.create(validated_data=data)

        # get tokens
        refresh_token = RefreshToken.for_user(user)
        access_token = AccessToken.for_user(user)

        partner = self.find_partner_guest(user)
        res = {
            'refresh_token': str(refresh_token),
            'access_token': str(access_token),
            'id': user.id,
        }

        if partner is not None:
            res['partner_id'] = partner.id
        else:
            res['partner_id'] = None

        import pdb
        pdb.set_trace()

        return Response(res)

    def find_partner_guest(self, user):

        try:
            partner = Partner.objects.get(
                phone_number=user.phone_number,
                phone_region_code=user.phone_region_code,
                is_active=False
            )
            return partner
        except:
            return None
