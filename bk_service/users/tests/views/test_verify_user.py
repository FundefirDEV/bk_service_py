""" Login test !"""

#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Utils
from bk_service.utils.loaddata.loaddata import setup_db

# Utils commons
from bk_service.users.tests.utils.commons import *


class VerifyEmailTestCase(APITestCase):
    """ Verify Email success test class """

    def setUp(self):

        setup_db(setup_db, only_locations=True)
        url = '/users/verify_email/'
        request = self.client.get(url, 'asdasd@mail.co', format='json')

    def test_verify_email_success(self):
        """ Verify Email success """

        url = '/users/verify_email/'

        request = self.client.get(url, login_data, format='json')
        body = request.data
        status_code = request.status_code

        # import pdb
        # pdb.set_trace()

        self.assertEqual(request.status_code, status.HTTP_200_OK)
