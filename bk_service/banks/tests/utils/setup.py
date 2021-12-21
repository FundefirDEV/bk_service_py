#  Django

from datetime import date
from bk_service.users.models.users import *
from bk_service.banks.models import *
from bk_service.requests.tests.utils.setup import *
from bk_service.locations.tests.utils.setup import create_locations

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


def create_credit():
    partner = create_partner()
    credit_request = create_credit_request(partner)
    credit = Credit.objects.create(bank=partner.bank, partner=partner,
                                   credit_request=credit_request, installments=credit_request.installments, amount=credit_request.amount)
    return credit


def create_schedule_installment():
    credit = create_credit()
    schedule_installment = ScheduleInstallment.objects.create(
        credit=credit, capital_installment=90000, ordinary_interest_percentage=1, interest_calculated=1000, total_pay_installment=0, payment_status='', payment_date=date.today())
    return schedule_installment


def create_payment_schedules():
    schedule_installment = create_schedule_installment()
    payment_schedule_request = create_payment_schedule_request(schedule_installment.credit, schedule_installment)
    payment_schedule = PaymentSchedule.objects.create(payment_schedule_request=payment_schedule_request, amount=payment_schedule_request.amount,
                                                      partner=payment_schedule_request.partner, bank=payment_schedule_request.bank, date=date.today())
    return payment_schedule
