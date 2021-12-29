""" Verify user !"""

#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail

# Utils
from bk_service.utils.loaddata.loaddata import setup_db
from bk_service.banks.tests.utils.setup import create_user
from bk_service.locations.tests.utils.setup import create_locations

# Utils commons
from bk_service.users.tests.utils.commons import *

# error
from bk_service.utils.constants_errors import *


# import pdb
# pdb.set_trace()


class VerifyEmailTestCase(APITestCase):
    """ Verify Email success test class """

    def setUp(self):
        city = create_locations()
        create_user(username='used@mail.com', email='used@mail.com', city=city)

    def test_verify_email_success(self):
        """ Verify Email success """

        url = '/users/verify-email/new@mail.com/'

        request = self.client.get(url, format='json')
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, 'email is valid')

    def test_verify_email_already_exist(self):
        """ Verify Email already exist """

        url = '/users/verify-email/used@mail.com/'

        request = self.client.get(url, format='json')
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(body, {
            'email':
            [ErrorDetail(string=build_error_message(EMAIL_EXIST), code='unique')]
        })


class VerifyPhoneTestCase(APITestCase):
    """ Verify Phone success test class """

    def setUp(self):
        city = create_locations()
        create_user(phone_number='3100000000', city=city)

    def test_verify_phone_success(self):
        """ Verify Phone success """

        url = '/users/verify-phone/311111111/'

        request = self.client.get(url, format='json')
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, 'phone is valid')

    def test_verify_phone_already_exist(self):
        """ Verify Phone already exist """

        url = '/users/verify-phone/3100000000/'

        request = self.client.get(url, format='json')
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(body, {
            'phone_number':
            [ErrorDetail(string=build_error_message(PHONE_EXIST), code='unique')]
        })
