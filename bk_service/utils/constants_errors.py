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
