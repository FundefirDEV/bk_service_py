#  Django

from bk_service.locations.tests.utils.setup import createLocations
from bk_service.users.models.users import User
from bk_service.banks.models.partners import Partner
from bk_service.banks.models.banks import Bank
from bk_service.banks.models.bank_rules import BankRules
from bk_service.banks.models.shares import Share

# import pdb
# pdb.set_trace()


def createBank():
    city = createLocations()
    bank = Bank.objects.create(name='new_bank', city=city)
    return bank


def createBankRules():
    bank = createBank()
    bank_rules = BankRules.objects.create(bank=bank)
    return bank


def createUser(city):
    user = User.objects.create_user(username='user@mail.com', email='user@mail.com',
                                    first_name='Bre', phone_number='31300000000', city=city, last_name='Bre')
    return user


def createPartner():
    bank = createBankRules()
    user = createUser(bank.city)
    partner = Partner.objects.create(bank=bank, user=user)
    return partner


def createShare():
    partner = createPartner()
    share = Share.objects.create(bank=partner.bank, partner=partner, quantity=1, amount=10000)
    return share
