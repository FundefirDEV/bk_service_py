""" Update user !"""

#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail

# Utils
from bk_service.utils.loaddata.loaddata import setup_db
from bk_service.banks.tests.utils.setup import create_user
from bk_service.locations.tests.utils.setup import create_locations
from bk_service.utils.tests.requests import post_with_token

# Utils commons
from bk_service.users.tests.utils.commons import *

# error
from bk_service.utils.constants_errors import *

from bk_service.users.models.users import User
# # import pdb
# pdb.set_trace()


class UpdateProfileTestCase(APITestCase):
    """ success test class """

    def setUp(self):
        city = create_locations()
        self.user = create_user(username='ejample@mail.com', email='ejample@mail.com', city=city)
        self.user2 = create_user(username='used@mail.com', email='used@mail.com', phone_number='3111111', city=city)

    def test_update_profile_success(self):
        """ success """
        url = '/users/update-profile/'
        body = {
            'username': 'new@mail.com',
            'first_name': 'new',
            'last_name': 'new',
            'email': 'new@mail.com',
            'phone_number': '300000000',
            'gender': 'F',
            'phone_region_code': '+57'
        }
        request = post_with_token(URL=url, user=self.user, body=body)
        user_validation = User.objects.get(username=body['username'])
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(user_validation.phone_number, body['phone_number'])
        self.assertEqual(user_validation.email, body['email'])
        self.assertEqual(user_validation.gender, body['gender'])
        self.assertEqual(user_validation.phone_region_code, body['phone_region_code'])

    def test_update_profile_fails_username_exist(self):
        """ success """
        url = '/users/update-profile/'
        body = {
            'username': 'used@mail.com',
            'first_name': 'new',
            'last_name': 'new',
            'email': 'new@mail.com',
            'phone_number': '300000000',
            'gender': 'F',
            'phone_region_code': '+57'
        }
        request = post_with_token(URL=url, user=self.user, body=body)
        self.assertEqual(request.status_code, 400)
