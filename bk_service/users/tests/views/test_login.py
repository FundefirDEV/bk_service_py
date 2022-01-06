""" Login test !"""

#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Utils
from bk_service.utils.loaddata.loaddata import setup_db

# Utils commons
from bk_service.users.tests.utils.commons import *


class LogInAPITestCase(APITestCase):
    """ Login success test class """

    def setUp(self):

        setup_db(setup_db, only_locations=True)
        url = '/users/singup/'
        request = self.client.post(url, singup_data, format='json')

    def test_Login_success(self):
        """ Login success """

        url = '/users/login/'

        request = self.client.post(url, login_data, format='json')
        body = request.data
        status_code = request.status_code

        # # import pdb
        # pdb.set_trace()

        access_token = body['access_token']
        refresh_token = body['refresh_token']
        # partner_id = body['partner_id']

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(access_token)
        self.assertIsNotNone(refresh_token)
        # self.assertIsNone(partner_id)


class LogInFailAPITestCase(APITestCase):
    """ Login fail test class """

    def setUp(self):
        setup_db(setup_db)

    def test_Login_bad_credentials(self):
        """ Login bad credentials test """

        url = '/users/login/'

        bad_data = login_data.copy()
        bad_data['password_confirmation'] = 'bad pass'

        request = self.client.post(url, bad_data, format='json')
        body = request.data
        status_code = request.status_code

        # # import pdb
        # pdb.set_trace()

        self.assertEqual(status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(str(body['detail']), "No active account found with the given credentials")
