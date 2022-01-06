from rest_framework.test import APITestCase
from bk_service.bk_core_sdk.bk_core_sdk_validations import BkCoreSDKValidations
from bk_service.banks.tests.utils.setup import create_partner
from bk_service.utils.exceptions_errors import CustomValidation


class MaximunNumberOfSharesTest(APITestCase):
    """ Test Maximun number of shares validations """

    def setUp(self):
        self.partner = create_partner()

    def test_maximun_number_of_shares_cero_quantity(self):
        bk_validation = BkCoreSDKValidations(partner=self.partner)

        self.assertRaises(error=QUANTITY_INVALID)
        bk_validation.maximun_number_of_shares(quantity=0)

        # import pdb
        # pdb.set_trace()
        self.assertEquals(1, 1)
