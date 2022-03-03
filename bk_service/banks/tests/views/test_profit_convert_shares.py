#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail

# Utils commons
from bk_service.utils.tests.requests import get_with_token, post_with_token

# Banks test Utils
from bk_service.banks.tests.utils.setup import *
from bk_service.requests.tests.utils.setup import *

# test-utils
from bk_service.utils.tests.test_security import security_test_post, security_test_partner_admin_post

URL = '/banks/profit-convert-shares/'
CLOSE_MEETING_URL = '/banks/meetings/close/'


class ProfitConvertSharesAPITestCase(APITestCase):
    """ profit payment convert shares test class """

    def setUp(self):

        self.partner = create_partner(role=PartnerType.admin)
        security_test_post(self=self, URL=URL)

        self.share_request = create_share_request(
            partner=self.partner, quantity=20, amount=200000
        )
        self.share = create_share(
            partner=self.partner,
            share_request=self.share_request
        )

        self.credit_request = create_credit_request(
            partner=self.partner,
            amount=100000,
            installments=3
        )

        self.credit = create_credit(partner=self.partner, credit_request=self.credit_request)
        self.schedule_installment = create_schedule_installment(self.credit)

        self.payment_schedule_request = create_payment_schedule_request(
            credit=self.credit,
            schedule_installment=self.schedule_installment
        )
        self.payment_schedule = create_payment_schedules(
            credit=self.credit,
            payment_schedule_request=self.payment_schedule_request
        )

        close_meeting = get_with_token(URL=CLOSE_MEETING_URL, user=self.partner.user,)

    def test_profit_convert_shares_success(self):
        """ test post profit payment success """

        security_test_partner_admin_post(
            self=self,
            URL=URL,
            body={
                'partner_id': 0,
                'earning_shares_ids': [0],
            }
        )
        earning_share_2 = create_earning_share(share=self.share, earning_by_share=1, total_earning_by_share=15000)
        earning_share_3 = create_earning_share(share=self.share, earning_by_share=1, total_earning_by_share=10000)

        pre_partner_detail = PartnerDetail.objects.get(partner=self.partner)
        pre_bank = Bank.objects.get(pk=self.partner.bank.id)

        request_body = {
            'partner_id': self.partner.id,
            'quantity': 2,
            'earning_shares_ids': [earning_share_2.id, earning_share_3.id],
        }

        request = post_with_token(URL=URL, user=self.partner.user, body=request_body)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_200_OK)

        new_earning_share_2 = EarningShare.objects.get(pk=earning_share_2.id)
        new_earning_share_3 = EarningShare.objects.get(pk=earning_share_3.id)

        self.assertEqual(new_earning_share_2.is_paid, True)
        self.assertEqual(new_earning_share_3.is_paid, True)

        profit_amount = new_earning_share_2.total_earning_by_share + new_earning_share_3.total_earning_by_share
        profit_amount = profit_amount - 20000

        new_partner_detail = PartnerDetail.objects.get(partner=self.partner)
        new_bank = Bank.objects.get(pk=self.partner.bank.id)

        self.assertEqual(new_partner_detail.earnings, pre_partner_detail.earnings - profit_amount)
        self.assertEqual(new_partner_detail.profit_obtained, pre_partner_detail.profit_obtained + profit_amount)
        self.assertEqual(new_bank.cash_balance, pre_bank.cash_balance - profit_amount)

        self.assertEqual(new_partner_detail.shares, pre_partner_detail.shares + 2)
