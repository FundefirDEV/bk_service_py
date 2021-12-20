""" Login test !"""

#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Utils
from bk_service.utils.loaddata.loaddata import setup_db

# Utils commons
from bk_service.users.tests.utils.commons import *


# class LogInAPITestCase(APITestCase):
#     """ Login test class """

#     def setUp(self):
#         setup_db(setup_db)

#     def test_Login_success(self):
#         """ Login success """

#         url = '/users/login/'

#         request = self.client.post(url, login_data, format='json')
#         body = request.data
#         status_code = request.status_code

#         import pdb
#         pdb.set_trace()

#         access_token = body['access_token']
#         refresh_token = body['refresh_token']
#         # partner_id = body['partner_id']

#         self.assertEqual(request.status_code, status.HTTP_200_OK)
#         self.assertIsNotNone(access_token)
#         self.assertIsNotNone(refresh_token)
# self.assertIsNone(partner_id)

# def test_Login_bad_pass_confirmation(self):
#     """ bad pass confirmation test """

#     url = '/users/Login/'

#     bad_data = Login_data.copy()
#     bad_data['password_confirmation'] = 'bad pass'

#     request = self.client.post(url, bad_data, format='json')
#     body = request.data
#     status_code = request.status_code

#     # import pdb
#     # pdb.set_trace()

#     self.assertEqual(status_code, status.HTTP_400_BAD_REQUEST)
#     self.assertEqual(str(body[0]), "Password don't match")
