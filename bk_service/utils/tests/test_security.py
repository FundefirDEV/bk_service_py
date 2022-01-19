#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APIClient

# Utils error
from bk_service.utils.constants_errors import build_error_message, PARTNER_IS_NOT_ADMIN

# Utils commoms
from bk_service.utils.tests.requests import get_with_token, post_with_token
from bk_service.banks.tests.utils.setup import create_bank, create_partner

# Utils enum
from bk_service.utils.enums.banks import PartnerType

# Models
from bk_service.locations.models.cities import City


def security_test_get(self, URL):
    """ Verify GET Request response 401"""
    client = APIClient()
    request = client.get(URL, format='json')
    body = request.data
    self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)
    self.assertEqual(body,
                     {'detail': ErrorDetail(
                         string='Authentication credentials were not provided.', code='not_authenticated')}
                     )


def security_test_post(self, URL):
    """ Verify POST Request response 401"""
    client = APIClient()
    request = client.post(URL, format='json')
    body = request.data
    self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)
    self.assertEqual(body,
                     {'detail': ErrorDetail(
                         string='Authentication credentials were not provided.', code='not_authenticated')}
                     )


def security_test_partner_admin_get(self, URL,):
    """ Verify GET partner not admin Request response 401"""
    client = APIClient()
    city = City.objects.first()
    bank = create_bank(city=city, name='not_admin_bank')
    partner = create_partner(
        role=PartnerType.partner,
        bank=bank,
        phone_number='345678876',
        email='notadminemail@mail.com'
    )
    request = get_with_token(URL=URL, user=partner.user,)

    body = request.data
    self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)
    self.assertEqual(body, {'detail': build_error_message(error=PARTNER_IS_NOT_ADMIN)})


def security_test_partner_admin_post(self, URL, body):
    """ Verify POST partner not admin Request response 401"""
    client = APIClient()
    city = City.objects.first()
    bank = create_bank(city=city, name='not_admin_bank')
    partner = create_partner(
        role=PartnerType.partner,
        bank=bank,
        phone_number='345678876',
        email='notadminemail@mail.com'
    )

    request = post_with_token(URL=URL, user=partner.user, body=body)

    body = request.data
    self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)
    self.assertEqual(body, {'detail': build_error_message(error=PARTNER_IS_NOT_ADMIN)})
