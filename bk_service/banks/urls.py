""" Users URLs. """

# Django
from django.urls import path

# Views
from bk_service.banks.views import (
    BankCreationAPIView,
    VerifyPartnerPhone,
    VerifyPartnerGuestPhone,
    DeletePartnerGuestAPIView,
    InvitePartnerGuestAPIView
)

urlpatterns = [
    path('banks/bank/', BankCreationAPIView.as_view(), name='bank_creation_view'),
    path('banks/verify_partner_phone/<str:phone_number>/', VerifyPartnerPhone.as_view(), name='verify_partner_phone_view'),
    path('banks/verify_partner_guest_phone/<str:phone_number>/',
         VerifyPartnerGuestPhone.as_view(), name='verify_partner_guest_phone_view'),

    path('banks/delete-partner-guest/',
         DeletePartnerGuestAPIView.as_view(),
         name='delete_partner_guest_view'),

    path('banks/invite-partner-guest/',
         InvitePartnerGuestAPIView.as_view(),
         name='invite_partner_guest_view'),

]
