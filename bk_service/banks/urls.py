""" Users URLs. """

# Django
from django.urls import path

# Views
from bk_service.banks.views import (
    BankCreationAPIView,
    VerifyPartnerPhone,
    VerifyPartnerGuestPhone,
    DeletePartnerGuestAPIView,
    VerifyMultiplePhones,
    InvitePartnerGuestAPIView,
    BankRule,
    BankDetail
)

urlpatterns = [
    path('banks/bank/', BankCreationAPIView.as_view(), name='bank_creation_view'),
    path('banks/verify-partner-phone/<str:phone_number>/', VerifyPartnerPhone.as_view(), name='verify_partner_phone_view'),
    path('banks/verify-partner-guest-phone/<str:phone_number>/',
         VerifyPartnerGuestPhone.as_view(), name='verify_partner_guest_phone_view'),
    path('banks/verify-multiple-phones/', VerifyMultiplePhones.as_view(), name='verify_partner_multiple_phones_view'),


    path('banks/delete-partner-guest/',
         DeletePartnerGuestAPIView.as_view(),
         name='delete_partner_guest_view'),

    path('banks/invite-partner-guest/',
         InvitePartnerGuestAPIView.as_view(),
         name='invite_partner_guest_view'),

    path('banks/bank-rules/', BankRule.as_view(), name="bank-rules"),
    path('banks/bank-detail/', BankDetail.as_view(), name="bank-details")


]
