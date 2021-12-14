# """ User views. """

# # Django REST Framework
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny


# # Simple JWT
# from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework_simplejwt.tokens import RefreshToken

# # Serializers
# from bk_service.users.serializers import MyTokenObtainPairSerializer, UserModelSerializer


# class UserLoginAPIView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer


# class UserSingUpAPIView(APIView):

#     permission_classes = [AllowAny]

#     def post(self, request, *args, **kwargs):
#         data = request.data
#         serializer = UserModelSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.create(validated_data=data)
#         token = RefreshToken.for_user(user)

#         res = {
#             'user': serializer.data,
#             'token': str(token)
#         }

#         return Response(res)
