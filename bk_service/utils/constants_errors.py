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


DEFAULD = Errors()

EMAIL_EXIST = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=1,
    error_mensage='This email already exists.'
)

PHONE_EXIST = Errors(
    status_code=status.HTTP_400_BAD_REQUEST,
    error_code=2,
    error_mensage='This phone already exists.'
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
