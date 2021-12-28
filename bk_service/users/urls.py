""" Users URLs. """

# Django
from django.urls import path, include

# Views
from bk_service.users.views import UserLoginAPIView, UserSingUpAPIView, VerifyEmail

urlpatterns = [
    path('users/login/', UserLoginAPIView.as_view(), name='login_view'),
    path('users/singup/', UserSingUpAPIView.as_view(), name='singup_view'),
    path('users/verify-email/<str:email>/', VerifyEmail.as_view(), name='verify_email_view'),

]
