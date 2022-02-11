# Django REST Framework
from rest_framework import status


class Errors():
    def __init__(
        self,
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        error_code=0,
        error_mensage='A server error occurred.'
    ):
        self.status_code = status_code
        self.error_mensage = error_mensage
        self.error_code = error_code


def build_error_message(error):
    return f"error_message : {str(error.error_mensage)}, error_code : {error.error_code}"


DEFAULD = Errors()

EMAIL_EXIST = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=1,
    error_mensage='This email already exists.'
)

PHONE_EXIST = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=2,
    error_mensage='This phone number already exists.'
)

USERNAME_EXIST = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=3,
    error_mensage='This username already exists.'
)

PASSWORD_TOO_COMMON = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=4,
    error_mensage='This password is too common.'
)

PASSWORD_CONFIRMATION = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=5,
    error_mensage="Password don't match."
)


EMAIL_REQUIRED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=6,
    error_mensage='The email is required.'
)

PHONE_REQUIRED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=7,
    error_mensage='The phone number is required.'
)

PASSWORD_REQUIRED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=8,
    error_mensage='The password is required.'
)

PASSWORD_CONFIRMATION_REQUIRED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=9,
    error_mensage='The password confirmation is required.'
)

PHONE_REGION_CODE_REQUIRED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=10,
    error_mensage='The phone region code is required.'
)


EMAIL_INVALID = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=11,
    error_mensage='The email is invalid.'
)

PHONE_INVALID = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=12,
    error_mensage='The phone number is invalid.'
)

PHONE_REGION_CODE_INVALID = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=13,
    error_mensage='The phone region code is invalid.'
)

USERNAME_INVALID = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=14,
    error_mensage='The username is invalid.'
)

CITY_REQUIRED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=15,
    error_mensage='The city is required.'
)

CITY_INVALID = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=16,
    error_mensage='The city is invalid.'
)


FIRST_NAME_REQUIRED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=17,
    error_mensage='The first name is required.'
)

LAST_NAME_REQUIRED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=18,
    error_mensage='The last name is required.'
)

FIRST_NAME_INVALID = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=19,
    error_mensage='The first name is invalid.'
)

LAST_NAME_INVALID = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=20,
    error_mensage='The last name is invalid.'
)

GENDER_REQUIRED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=21,
    error_mensage='The gender is required.'
)

GENDER_INVALID = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=22,
    error_mensage='The gender is invalid.'
)

USERNAME_INVALID = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=23,
    error_mensage='The username is invalid.'
)

USERNAME_REQUIRED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=24,
    error_mensage='The username is required.'
)

PASSWORD_INVALID = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=25,
    error_mensage='The password is invalid.'
)

PASSWORD_CONFIRMATION_INVALID = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=26,
    error_mensage='The password confirmation is invalid.'
)

BANK_NAME_REQUIRED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=27,
    error_mensage='The bank name is required.'
)

BANK_NAME_EXIST = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=28,
    error_mensage='This bank name already exists.'
)

PARTNER_GUEST_NAME_REQUIRED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=29,
    error_mensage='The partner guest name is required.'
)

PARTNER_GUEST_PHONE_REQUIRED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=30,
    error_mensage='The partner guest phone number is required.'
)

PARTNER_GUEST_PHONE_EXIST = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=31,
    error_mensage='This partner guest phone already exists.'
)

PARTNER_GUEST_PHONE_REGION_CODE_REQUIRED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=32,
    error_mensage='The partner guest phone region code is required.'
)

PARTNER_GUEST_NAME_INVALID = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=33,
    error_mensage='The partner guest name is invalid.'
)

PARTNER_GUEST_PHONE_INVALID = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=34,
    error_mensage='The partner guest phone is invalid.'
)
PARTNER_GUEST_PHONE_REGION_CODE_INVALID = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=35,
    error_mensage='The partner guest phone region code is invalid.'
)

BANK_NAME_INVALID = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=36,
    error_mensage='The bank name is invalid.'
)

BANK_INVALID = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=37,
    error_mensage='The bank is invalid.'
)

BANK_REQUIRED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=38,
    error_mensage='The bank is required.'
)

USER_INVALID = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=39,
    error_mensage='The user is invalid.'
)

USER_REQUIRED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=40,
    error_mensage='The user is required.'
)

PARTNER_ROLE_INVALID = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=41,
    error_mensage='The partner role is invalid.'
)

PARTNER_ROLE_REQUIRED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=42,
    error_mensage='The partner role is required.'
)

PARTNER_GUEST_NOT_EXIST = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=43,
    error_mensage='This partner guest no exist.'
)


TYPE_REQUEST_REQUIRED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=44,
    error_mensage='The type request is required.'
)

TYPE_REQUEST_INVALID = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=45,
    error_mensage='The type request is invalid.'
)

AMOUNT_REQUIRED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=46,
    error_mensage='The amount is required.'
)

AMOUNT_INVALID = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=47,
    error_mensage='The amount is invalid.'
)

QUANTITY_REQUIRED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=48,
    error_mensage='The quantity is required.'
)

QUANTITY_INVALID = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=49,
    error_mensage='The quantity is invalid.'
)

ID_CREDIT_REQUIRED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=50,
    error_mensage='The id credit is required.'
)

ID_CREDIT_INVALID = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=51,
    error_mensage='The id credit is invalid.'
)

ID_CREDIT_NOT_EXIST = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=52,
    error_mensage='This id credit no exist.'
)

CREDIT_USE_REQUIRED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=53,
    error_mensage='The credit use is required.'
)

CREDIT_USE_INVALID = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=54,
    error_mensage='The credit use is invalid.'
)

DETAIL_REQUIRED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=55,
    error_mensage='The detail is required.'
)

DETAIL_INVALID = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=56,
    error_mensage='The detail is invalid.'
)

PAYMENT_TYPE_REQUIRED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=57,
    error_mensage='The payment type is required.'
)

PAYMENT_TYPE_INVALID = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=58,
    error_mensage='The payment type is invalid.'
)

ID_SCHEDULE_INSTALMENT_REQUIRED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=59,
    error_mensage='The id schedule instalment is required.'
)

ID_SCHEDULE_INSTALMENT_INVALID = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=60,
    error_mensage='The id schedule instalment is invalid.'
)

ID_SCHEDULE_INSTALMENT_NOT_EXIST = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=61,
    error_mensage='This id schedule instalment no exist.'
)

MAXIMUN_NUMBER_OF_SHARES = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=62,
    error_mensage='Maximun number of shares exceeded'
)

ID_REQUESTS_NOT_EXIST = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=63,
    error_mensage='This id requests no exist.'
)

ID_REQUESTS_REQUIRED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=64,
    error_mensage='The id requests is required.'
)

ID_REQUESTS_INVALID = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=65,
    error_mensage='The id requests is invalid.'
)

APPROVALS_STATUS_REQUIRED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=66,
    error_mensage='The approvals status is required.'
)

APPROVALS_STATUS_INVALID = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=67,
    error_mensage='The approvals status is invalid.'
)

PARTNER_IS_NOT_ADMIN = Errors(
    status_code=status.HTTP_401_UNAUTHORIZED,
    error_code=68,
    error_mensage='This partner is not admin.'
)

PENDING_REQUEST = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=69,
    error_mensage='This partner already have a pending request'
)

CASH_BALANCE_EXCCEDED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=70,
    error_mensage='Request quantity exceed Cash balance '
)

MAX_CREDIT_EXCCEDED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=71,
    error_mensage='Request quantity exceed maximun credit value '
)

MAX_PARTNER_CREDIT_EXCCEDED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=72,
    error_mensage='Request quantity exceed maximun credit value of this partner '
)
MAX_CREDIT_INSTALLMENTS_EXCCEDED = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=73,
    error_mensage='Credit Request installments exceed'
)
CHANGE_RULES_PENDING_REQUEST = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=74,
    error_mensage="Can't change rules with pending requests"
)
