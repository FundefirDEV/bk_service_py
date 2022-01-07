# Django REST Framework
from rest_framework.exceptions import APIException
from rest_framework import status

# Utils
from bk_service.utils.constants_errors import Errors, DEFAULD, build_error_message


class CustomException(APIException):
    def __init__(self, error=DEFAULD):
        self.status_code = error.status_code
        self.error_code = error.error_code
        self.detail = build_error_message(error)
