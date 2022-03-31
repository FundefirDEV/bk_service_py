""" Users URLs. """

# Django
from django.urls import path

# Views
from bk_service.banks.views import *

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

    path('banks/bank-rules/', BankRuleApiView.as_view(), name="bank-rules"),
    path('banks/bank-detail/', BankDetailAPIView.as_view(), name="bank-details"),
    path('banks/partners/', PartnerAPIView.as_view(), name="bank-partners"),

    path('banks/profile/', ProfileAPIView.as_view(), name="profile"),

    path('banks/approvals/', ApprovalsAPIView.as_view(), name="approvals"),

    path('banks/special-credit/', SpecialCreditAPIView.as_view(), name="special_credit"),

    path('banks/meetings/', MeetingsGetAPIView.as_view(), name="meetings"),
    path('banks/meetings/close/', CloseMeetingsAPIView.as_view(), name="close_meetings"),

    path('banks/my-bank-info/', MyBankInfoAPIView.as_view(), name="my-bank-info"),
    path('banks/shares-current-meeting/', SharesCurrentMeetingAPIView.as_view(), name="shares-current-meeting"),
    path('banks/credits-current-meeting/', CreditsCurrentMeetingAPIView.as_view(), name="credits-current-meeting"),
    path('banks/partner-admin/', PartnerAdminApiView.as_view(), name="partner-admin"),


    path('banks/profit-payment-partners/', ProfitPaymentPartnersAPIView.as_view(), name="profit-payment-partners"),
    path('banks/profit-payment/<int:partner_id>/', ProfitPaymentAPIView.as_view(), name="profit-payment-partner-id"),
    path('banks/profit-payment/', ProfitPaymentAPIView.as_view(), name="profit-payment"),
    path('banks/profit-convert-shares/', ProfitConvertSharesAPIView.as_view(), name="profit-convert-shares"),


    path('banks/my-shares/', SharesModelAPIView.as_view(), name="my-shares"),
    path('banks/my-credit/', CreditModelAPIView.as_view(), name="my-credit"),
    path('banks/my-payment-schedule/', PaymentScheduleModelAPIView.as_view(), name="my-payment-schedule"),
    path('banks/my-earning-shares/', EarningShareModelAPIView.as_view(), name="my-earning-shares"),

    path('banks/reports/', ReportsAPIView.as_view(), name="reports"),

]
