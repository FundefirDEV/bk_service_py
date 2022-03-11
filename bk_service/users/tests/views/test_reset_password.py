""" Reset password !"""

from django_rest_passwordreset.models import ResetPasswordToken

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


class ResetPassword(APITestCase):
    """ reset password success test class """

    def setUp(self):
        city = create_locations()
        self.user = create_user(username='user@mail.com', email='user@mail.com', city=city)

    def test_verify_email_success(self):
        """ Verify Email success """

        url = '/users/reset-password/'
        body = {
            'email': 'user@mail.com'
        }

        request = self.client.post(url, format='json', data=body)
        body = request

        self.assertEqual(request.status_code, status.HTTP_200_OK)

        token = ResetPasswordToken.objects.last().key
        new_password = "new_password_321"

        body_token_confirmation = {
            "token": token,
            "password": new_password
        }

        token_confirmation_url = url + "confirm/?token=" + token

        response_token_confirmation = self.client.post(
            path=token_confirmation_url,
            data=body_token_confirmation,
            format='json')
        self.assertEqual(response_token_confirmation.status_code, 200)

        # test login with new password
        body_login = {
            "email": self.user.username,
            "password": new_password
        }

        response_login = self.client.post(
            path='/users/login/',
            data=body_login,
            format='json')

        self.assertEqual(response_login.status_code, 200)
        self.assertContains(response_login, "token")
