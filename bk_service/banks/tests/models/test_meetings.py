""" Meeting Test. """

#  Django
from django.test import TestCase
from bk_service.banks.models.meetings import Meeting
# Utils
from bk_service.banks.tests.utils.setup import create_meeting, create_bank


class MeetingTestCase(TestCase):
    """ Meeting test class """

    def test_meeting_success(self):
        bank = create_bank()
        meeting_created = create_meeting(bank=bank)
        meeting = Meeting.objects.get(id=meeting_created.id)

        self.assertEqual(meeting.bank, meeting_created.bank)
        self.assertEqual(meeting.total_shares_quantity, 0)
        self.assertEqual(meeting.total_credits_quantity, 0)
        self.assertEqual(meeting.total_shares_amount, 0.0)
        self.assertEqual(meeting.total_credits_amount, 0.0)
        self.assertEqual(meeting.total_ordinary_interest, 0)
        self.assertEqual(meeting.total_capital, 0)
        self.assertEqual(meeting.total_delay_interest, 0)
        self.assertEqual(meeting.earning_by_share, 0)
        # self.assertEqual(meeting.balance, 0)
        self.assertEqual(meeting.expenditure_fund, 0)
        self.assertEqual(meeting.reserve_fund_of_bad_debt, 0)
