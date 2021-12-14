""" Users URLs. """

# Django
from django.urls import path

# Views
from bk_service.pings.views import PingAPIView

urlpatterns = [
    path('ping/', PingAPIView.as_view(), name='ping'),
]
