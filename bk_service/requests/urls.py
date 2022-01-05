""" Users URLs. """

# Django
from django.urls import path, include

# Views
from bk_service.requests.views import RequestsAPIView

urlpatterns = [
    path('requests/requests/', RequestsAPIView.as_view(), name='request_view'),
]
