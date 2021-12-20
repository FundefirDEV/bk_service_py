""" SingUp test !"""

#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Utils
from bk_service.utils.loaddata.loaddata import setup_db

# Utils commons
from bk_service.users.tests.utils.commons import *


class SingUpAPITestCase(APITestCase):
    """ singup test class """

    def setUp(self):
        setup_db(setup_db)

    def test_singup_success(self):
        """ singup success """

        url = '/users/singup/'

        request = self.client.post(url, singup_data, format='json')
        body = request.data
        status_code = request.status_code

        # import pdb
        # pdb.set_trace()

        access_token = body['access_token']
        refresh_token = body['refresh_token']
        partner_id = body['partner_id']

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(access_token)
        self.assertIsNotNone(refresh_token)
        self.assertIsNone(partner_id)

    def test_singup_bad_pass_confirmation(self):
        """ bad pass confirmation test """

        url = '/users/singup/'

        bad_data = singup_data.copy()
        bad_data['password_confirmation'] = 'bad pass'

        request = self.client.post(url, bad_data, format='json')
        body = request.data
        status_code = request.status_code

        # import pdb
        # pdb.set_trace()

        self.assertEqual(status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(str(body[0]), "Password don't match")

    def test_singup_pass_too_commun(self):
        """ bad pass confirmation test """

        url = '/users/singup/'

        bad_data_pass_commun = singup_data.copy()
        bad_data_pass_commun['password_confirmation'] = 'admin1234'
        bad_data_pass_commun['password'] = 'admin1234'

        request = self.client.post(url, bad_data_pass_commun, format='json')
        body = request.data
        status_code = request.status_code

        # import pdb
        # pdb.set_trace()

        self.assertEqual(status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(str(body[0]), "This password is too common")
