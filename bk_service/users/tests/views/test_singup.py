""" SingUp test !"""

#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail

# Utils
from bk_service.utils.loaddata.loaddata import setup_db

# Utils commons
from bk_service.users.tests.utils.commons import *
from bk_service.locations.tests.utils.setup import create_locations

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


class SingUpWithPartnerSuccessAPITestCase(APITestCase):
    """ singup with partner success test class """

    def test_singup_with_partner_success(self):
        """ singup with partner success """

        url = '/users/singup/'
        partner = create_partner()
        partner_guest = invite_partner(
            bank=partner.bank,
            phone_number=singup_data['phone_number'],
            phone_region_code=singup_data['phone_region_code'])

        my_singup_data = dict(singup_data)
        my_singup_data['city'] = partner.user.city.id

        request = self.client.post(url, my_singup_data, format='json')

        body = request.data

        status_code = request.status_code

        access_token = body['access_token']
        refresh_token = body['refresh_token']
        partner_id = body['partner_id']
        user_id = body['id']

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(access_token)
        self.assertIsNotNone(refresh_token)
        self.assertIsNotNone(partner_id)
        self.assertIsNotNone(user_id)


class SingUpFailAPITestCase(APITestCase):
    """ singup fail test class """

    city_id = 0
    my_singup_data = dict(singup_data)

    def setUp(self):
        city = create_locations()
        self.city_id = city.id
        self.my_singup_data = dict(singup_data)
        self.my_singup_data['city'] = self.city_id

    def test_singup_bad_pass_confirmation(self):
        """ bad pass confirmation test """

        url = '/users/singup/'

        bad_data = self.my_singup_data.copy()
        bad_data['password_confirmation'] = 'bad pass'

        request = self.client.post(url, bad_data, format='json')
        body = request.data
        status_code = request.status_code

        # # import pdb
        # pdb.set_trace()

        self.assertEqual(status_code, status.HTTP_400_BAD_REQUEST)
        # self.assertEqual(body, {'error': "Password don't match.", 'error_code': 5})
        self.assertEqual(body, {'detail': build_error_message(error=PASSWORD_CONFIRMATION)})

    def test_singup_pass_too_commun(self):
        """ pass too commun test """

        url = '/users/singup/'

        bad_data_pass_commun = self.my_singup_data.copy()
        bad_data_pass_commun['password_confirmation'] = 'admin1234'
        bad_data_pass_commun['password'] = 'admin1234'

        request = self.client.post(url, bad_data_pass_commun, format='json')
        body = request.data
        status_code = request.status_code

        # # import pdb
        # pdb.set_trace()

        self.assertEqual(status_code, status.HTTP_400_BAD_REQUEST)
        # self.assertEqual(body, {'error': 'This password is too common.', 'error_code': 4})
        self.assertEqual(body, {'detail': build_error_message(error=PASSWORD_TOO_COMMON)})


class SingUpInvalidRequestAPITestCase(APITestCase):
    """ singup invalid request test class """

    city_id = 0

    def setUp(self):
        partner = create_partner()
        self.city_id = partner.user.city.id

    def test_singup_required_fields(self):
        """ singup required test """

        url = '/users/singup/'

        bad_data = {
            "bad_key": "bad_data",
        }

        request = self.client.post(url, bad_data, format='json')
        body = request.data
        status_code = request.status_code

        # # import pdb
        # pdb.set_trace()

        self.assertEqual(status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            body,
            {
                'email':
                    [ErrorDetail(string=build_error_message(EMAIL_REQUIRED), code='required')],
                'username':
                    [ErrorDetail(string=build_error_message(USERNAME_REQUIRED), code='required')],
                'gender':
                    [ErrorDetail(string=build_error_message(GENDER_REQUIRED), code='required')],
                'phone_number':
                    [ErrorDetail(string=build_error_message(PHONE_REQUIRED), code='required')],
                'phone_region_code':
                    [ErrorDetail(string=build_error_message(PHONE_REGION_CODE_REQUIRED), code='required')],
                'city':
                    [ErrorDetail(string=build_error_message(CITY_REQUIRED), code='required')],
                'password':
                    [ErrorDetail(string=build_error_message(PASSWORD_REQUIRED), code='required')],
                'password_confirmation':
                    [ErrorDetail(string=build_error_message(PASSWORD_CONFIRMATION_REQUIRED), code='required')]
            }
        )

    def test_singup_unique_fields(self):
        """singup unique test """

        url = '/users/singup/'

        bad_singup_data = dict(singup_data)
        bad_singup_data['username'] = 'user@mail.com'
        bad_singup_data['email'] = 'user@mail.com'
        bad_singup_data['phone_number'] = '31300000000'
        bad_singup_data['city'] = self.city_id

        request = self.client.post(url, bad_singup_data, format='json')
        body = request.data
        status_code = request.status_code

        # # import pdb
        # pdb.set_trace()

        self.assertEqual(status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            body,
            {
                'email':
                    [ErrorDetail(string=build_error_message(EMAIL_EXIST), code='unique')],
                'username':
                    [ErrorDetail(string=build_error_message(USERNAME_EXIST), code='unique')],
                'phone_number':
                    [ErrorDetail(string=build_error_message(PHONE_EXIST), code='unique')],
            }
        )
