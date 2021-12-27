""" Users URLs. """

# Django
from django.urls import path

# Views
from bk_service.banks.views import BankCreationAPIView

urlpatterns = [
    path('banks/bank/', BankCreationAPIView.as_view(), name='bank_creation_view'),
]
