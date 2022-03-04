""" E2E one meeting test !"""

#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail


# Utils commons
from bk_service.users.tests.utils.commons import *
from bk_service.locations.tests.utils.setup import create_locations
from bk_service.utils.tests.requests import get_with_token, post_with_token

# Banks test Utils
from bk_service.banks.tests.utils.setup import *
from bk_service.utils.tests.test_security import security_test_post

# Models
from bk_service.banks.models import *
from bk_service.requests.models import *
from bk_service.users.models.users import *

CREATE_BANK_URL = '/banks/bank/'


class E2EOneMeetingAPITestCase(APITestCase):
    """ Bank success test class """

    def setUp(self):
        security_test_post(self=self, URL=CREATE_BANK_URL)
        city = create_locations()
        self.user = create_user(city)
        self.city_id = city.id
        self.guests = [
            {
                "name": "Gibs",
                "phone_number": "3138129220",
                "phone_region_code": PHONE_REGION_CODE_TEST
            },
            {
                "name": "Alex",
                "phone_number": "3138129221",
                "phone_region_code": PHONE_REGION_CODE_TEST
            },
            {
                "name": "Jaime",
                "phone_number": "3138129222",
                "phone_region_code": PHONE_REGION_CODE_TEST
            }
        ]

    def test_one_meeting_success(self):
        """ Bank success and basic rules creation"""

        request_data = bank_creation_data(city_id=self.city_id, partners_guest=self.guests)

        request = post_with_token(URL=CREATE_BANK_URL, user=self.user, body=request_data)

        body = request.data
        status_code = request.status_code

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, {"message": "Bank created"})

        bank = self.user.partner.bank
        bank_rules = bank.get_bank_rules()
        rules_verification = BankRules.objects.get(bank=bank)

        partners_guest = PartnerGuest.objects.all()
        partner = Partner.objects.get(bank_id=bank.id)

        self.assertEqual(bank.name, BANK_NAME_TEST)
        self.assertEqual(len(partners_guest), 3)
        self.assertEqual(partner.user, self.user)
        self.assertEqual(rules_verification, bank_rules)
        self.assertEqual(bank_rules.bank, bank)

        """ singup success with guests partners """

        url_singup = '/users/singup/'
        counter = 1

        for guest in self.guests:
            counter += 1
            singup_data = {
                "password": PASSWORD_TEST,
                "password_confirmation": PASSWORD_TEST,
                "first_name": guest["name"],
                "last_name": "Manaos",
                "gender": "M",
                "city": self.city_id,
                "phone_number": guest["phone_number"],
                "phone_region_code": "+1",
                "email": guest["name"]+"@mail.com",
                "username": guest["name"]+"@mail.com"
            }

            request = self.client.post(url_singup, singup_data, format='json')
            body = request.data
            status_code = request.status_code

            access_token = body['access_token']
            refresh_token = body['refresh_token']
            partner_id = body['partner_id']
            user_id = body['id']

            partner_from_partner_guest = Partner.objects.get(phone_number=guest["phone_number"])

            self.assertEqual(request.status_code, status.HTTP_200_OK)

            self.assertEqual(partner_from_partner_guest.bank, bank)
            self.assertEqual(partner_from_partner_guest.is_active, True)
            self.assertEqual(partner_from_partner_guest.phone_region_code, guest["phone_region_code"])
            self.assertEqual(partner_from_partner_guest.role, PartnerType.partner)

            self.assertIsNotNone(access_token)
            self.assertIsNotNone(refresh_token)
            self.assertIsNotNone(partner_id)
            self.assertIsNotNone(user_id)

        """ Request Shares """
        url_request_shares = '/requests/requests/'

        body_request_shares = {
            'type_request': 'share',
            'quantity': 10
        }
        partners = Partner.objects.filter(bank=bank)
        for partner in partners:
            request = post_with_token(URL=url_request_shares, user=partner.user, body=body_request_shares)
            body = request.data
            status_code = request.status_code
            self.assertEqual(request.status_code, status.HTTP_200_OK)
            self.assertEqual(body, 'share request success !')

        """ Approve Shares """
        shares_requests = ShareRequest.objects.filter(bank=bank)
        self.assertEqual(bank.cash_balance, 0)
        self.assertEqual(len(shares_requests), len(partners))
        url_share_request = '/banks/approvals/'
        for share_request in shares_requests:
            approve_shares_body = {
                'type_request': 'share',
                'request_id': share_request.id,
                'approval_status': 'approved'
            }
            share_request_response = post_with_token(
                URL=url_share_request,
                user=self.user,
                body=approve_shares_body)
            body = share_request_response.data
            self.assertEqual(share_request_response.status_code, status.HTTP_200_OK)
            self.assertEqual(body, 'share approved success !')
        bank = Bank.objects.last()
        self.assertEqual(bank.cash_balance, 400000)

        """ Request Credits """
        url_request_credit = '/requests/requests/'
        for partner in partners:
            body_request_credits = {
                'type_request': 'credit',
                'amount': 100000,
                'quantity': 3,
                'credit_use': CreditUse.generationIncome,
                'credit_use_detail': CreditUseDetail.trade,
                'payment_type': CreditPayType.installments
            }
            request = post_with_token(URL=url_request_credit, user=partner.user, body=body_request_credits)
            body = request.data
            self.assertEqual(request.status_code, status.HTTP_200_OK)
            self.assertEqual(body, 'credit request success !')
        bank = Bank.objects.last()
        self.assertEqual(bank.cash_balance, 400000)

        """ Approve Credits """
        credits_requests = CreditRequest.objects.filter(bank=bank)
        for credit_request in credits_requests:
            approve_credits_body = {
                'type_request': 'credit',
                'request_id': credit_request.id,
                'approval_status': 'approved'
            }
            credit_request_response = post_with_token(
                URL=url_share_request,
                user=self.user,
                body=approve_credits_body)
            body = credit_request_response.data
            self.assertEqual(credit_request_response.status_code, status.HTTP_200_OK)
            self.assertEqual(body, 'credit approved success !')
        bank = Bank.objects.first()
        self.assertEqual(bank.cash_balance, 0)
