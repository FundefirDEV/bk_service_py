#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail

# Utils commons
from bk_service.utils.tests.requests import post_with_token

# Banks test Utils
from bk_service.banks.tests.utils.setup import *
from bk_service.requests.tests.utils.setup import *

# test-utils
from bk_service.utils.tests.test_security import (
    security_test_post,
    security_test_partner_admin_post
)

# Models
from bk_service.banks.models import Bank, PartnerDetail, Share

# Utils
from bk_service.utils.enums.requests import ApprovalStatus

# Utils Enums
from bk_service.utils.enums.banks import PartnerType

URL = '/banks/approvals/'


class ShareApprovalsAPITestCase(APITestCase):
    """ Share approvals test class """

    def setUp(self):
        self.partner = create_partner(role=PartnerType.admin)
        self.share_request = create_share_request(
            partner=self.partner, quantity=20, amount=200000
        )
        security_test_post(self=self, URL=URL)
        security_test_partner_admin_post(
            self=self,
            URL=URL,
            body={
                'type_request': 'share',
                'request_id': self.share_request.id,
                'approval_status': 'approved'
            }
        )

    def test_share_approvals_approve_requests_success(self):
        """ Share approvals approve requests success """

        request_body = {
            'type_request': 'share',
            'request_id': self.share_request.id,
            'approval_status': 'approved'
        }

        request = post_with_token(URL=URL, user=self.partner.user, body=request_body)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, 'share approved success !')

        share = Share.objects.get(share_request=self.share_request)

        self.assertEqual(share.quantity, 20)
        self.assertEqual(share.amount, 200000)
        self.assertEqual(share.partner, self.partner)
        self.assertEqual(share.bank, self.partner.bank)

        partner_detail = self.partner.partner_detail()

        self.assertEqual(partner_detail.shares, 20)
        self.assertEqual(partner_detail.partner.bank.shares, 20)
        self.assertEqual(partner_detail.partner.bank.cash_balance, 200000.0)

    def test_share_approvals_reject_requests_success(self):
        """ Share approvals reject requests success """

        request_body = {
            'type_request': 'share',
            'request_id': self.share_request.id,
            'approval_status': 'rejected'
        }

        request = post_with_token(URL=URL, user=self.partner.user, body=request_body)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(body, 'share rejected success !')

        share_request = ShareRequest.objects.get(pk=self.share_request.id)

        self.assertEqual(share_request.quantity, 20)
        self.assertEqual(share_request.amount, 200000)
        self.assertEqual(share_request.approval_status, ApprovalStatus.rejected)
        self.assertEqual(share_request.partner, self.partner)
        self.assertEqual(share_request.bank, self.partner.bank)

        partner_detail = self.partner.partner_detail()
        share_request = ShareRequest.objects.get(partner=self.partner, bank=self.partner.bank)

        self.assertEqual(partner_detail.shares, 0)
        self.assertEqual(partner_detail.partner.bank.shares, 0)
        self.assertEqual(partner_detail.partner.bank.cash_balance, 0)

    def test_share_approvals_fail_without_share_requests(self):
        """ Share approvals approve fail without share request """

        request_body = {
            'type_request': 'share',
            'request_id': 'bad_id',
            'approval_status': 'approved'
        }

        request = post_with_token(URL=URL, user=self.partner.user, body=request_body)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(body, {'detail': build_error_message(error=ID_REQUESTS_INVALID)})

        partner_detail = self.partner.partner_detail()
        share_request = ShareRequest.objects.get(partner=self.partner, bank=self.partner.bank)

        self.assertEqual(partner_detail.shares, 0)
        self.assertEqual(partner_detail.partner.bank.shares, 0)
        self.assertEqual(partner_detail.partner.bank.cash_balance, 0.0)

    def test_share_approvals_fail_partner_not_admin(self):
        """ Share approvals approve fail without share request """

        self.partner.role = PartnerType.partner
        self.partner.save()

        request_body = {
            'type_request': 'share',
            'request_id': self.share_request.id,
            'approval_status': 'approved'
        }

        request = post_with_token(URL=URL, user=self.partner.user, body=request_body)
        body = request.data

        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(body, {'detail': build_error_message(error=PARTNER_IS_NOT_ADMIN)})

        partner_detail = self.partner.partner_detail()
        share_request = ShareRequest.objects.get(partner=self.partner, bank=self.partner.bank)

        self.assertEqual(partner_detail.shares, 0)
        self.assertEqual(partner_detail.partner.bank.shares, 0)
        self.assertEqual(partner_detail.partner.bank.cash_balance, 0.0)
