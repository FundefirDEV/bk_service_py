""" SingUp test !"""

#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Utils
from bk_service.utils.loaddata.loaddata import setup_db

# Utils commons
from bk_service.users.tests.utils.commons import *

# Banks test Utils
from bk_service.banks.tests.utils.setup import *


class SingUpSuccessAPITestCase(APITestCase):
    """ singup success test class """

    def setUp(self):
        setup_db(setup_db, only_locations=True)

    def test_singup_success(self):
        """ singup success """

        url = '/users/singup/'

        request = self.client.post(url, singup_data, format='json')

        body = request.data
        status_code = request.status_code

        access_token = body['access_token']
        refresh_token = body['refresh_token']
        partner_id = body['partner_id']
        user_id = body['id']

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(access_token)
        self.assertIsNotNone(refresh_token)
        self.assertIsNone(partner_id)
        self.assertIsNotNone(user_id)


# class SingUpWithPartnerSuccessAPITestCase(APITestCase):
#     """ singup with partner success test class """

#     def setUp(self):
#         create_partner()

#     def test_singup_success(self):
#         """ singup success """

#         url = '/users/singup/'
#         partner = create_partner()

#         request = self.client.post(url, singup_data, format='json')

#         body = request.data
#         status_code = request.status_code

#         access_token = body['access_token']
#         refresh_token = body['refresh_token']
#         partner_id = body['partner_id']
#         user_id = body['id']

#         self.assertEqual(request.status_code, status.HTTP_200_OK)
#         self.assertIsNotNone(access_token)
#         self.assertIsNotNone(refresh_token)
#         self.assertIsNotNone(partner_id)
#         self.assertIsNotNone(user_id)


class SingUpFailAPITestCase(APITestCase):
    """ singup fail test class """

    def setUp(self):
        setup_db(setup_db)

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
