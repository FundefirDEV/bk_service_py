#  Django

from bk_service.users.models.users import User
from bk_service.banks.models.partners import Partner
from bk_service.banks.models.banks import Bank
from bk_service.banks.models.bank_rules import BankRules
from bk_service.banks.models.shares import Share
from bk_service.locations.tests.utils.setup import create_locations
from bk_service.requests.tests.utils.setup import create_share_request

# import pdb
# pdb.set_trace()


def create_bank():
    city = create_locations()
    bank = Bank.objects.create(name='new_bank', city=city)
    return bank


def create_bankRules():
    bank = create_bank()
    bank_rules = BankRules.objects.create(bank=bank)
    return bank


def create_user(city):
    user = User.objects.create_user(username='user@mail.com', email='user@mail.com',
                                    first_name='Bre', phone_number='31300000000', city=city, last_name='Bre')
    return user


def create_partner():
    bank = create_bankRules()
    user = create_user(bank.city)
    partner = Partner.objects.create(bank=bank, user=user)
    return partner


def create_share():
    partner = create_partner()
    share_request = create_share_request(partner)
    share = Share.objects.create(bank=partner.bank, share_request=share_request,
                                 partner=partner, quantity=1, amount=10000)
    return share
