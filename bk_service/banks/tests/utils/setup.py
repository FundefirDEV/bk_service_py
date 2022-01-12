
# Datetime
from datetime import date

# Models
from bk_service.users.models.users import *
from bk_service.banks.models import *

# Utils SetUp
from bk_service.requests.tests.utils.setup import *
from bk_service.locations.tests.utils.setup import create_locations

# Utils Enums
from bk_service.utils.enums.banks import PartnerType

# # import pdb
# pdb.set_trace()


PASSWORD_TEST = 'superSecurePassword2020'
USERNAME_TEST = 'user@mail.com'
PHONE_TEST = '31300000000'
PHONE_REGION_CODE_TEST = '+1'
FIRST_NAME_TEST = 'Brea'
LAST_NAME_TEST = 'Brea'

BANK_NAME_TEST = 'new_bank'
PARTNER_GUEST_NAME_TEST = 'new_partner_guest'
PARTNER_GUEST_PHONE_TEST = '31300000001'


def create_bank():
    city = create_locations()
    bank = Bank.objects.create(name=BANK_NAME_TEST, city=city)
    return bank


def create_user(
    city,
    username=USERNAME_TEST,
    email=USERNAME_TEST,
    password=PASSWORD_TEST,
    first_name=FIRST_NAME_TEST,
    phone_number=PHONE_TEST,
    phone_region_code=PHONE_REGION_CODE_TEST,
    last_name=LAST_NAME_TEST
):

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        phone_number=phone_number,
        phone_region_code=phone_region_code,
        city=city,
        last_name=last_name,
    )
    return user


def create_partner(phone_number=PHONE_TEST, role=PartnerType.partner):
    bank = create_bank()
    user = create_user(city=bank.city, phone_number=phone_number)
    partner = Partner.objects.create(
        bank=bank,
        user=user,
        phone_number=user.phone_number,
        role=role
    )
    return partner


def invite_partner(
    bank,
    name=PARTNER_GUEST_NAME_TEST,
    phone_number=PARTNER_GUEST_PHONE_TEST,
    phone_region_code=PHONE_REGION_CODE_TEST,
):
    partner_guest = PartnerGuest.objects.create(
        bank=bank,
        name=name,
        phone_number=phone_number,
        phone_region_code=phone_region_code,
        is_active=False
    )

    return partner_guest


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


def create_meeting(bank):
    meeting = Meeting.objects.create(bank=bank, date_meeting=date.today())
    return meeting


def create_earning_share():
    share = create_share()
    meeting = Meeting.objects.create(bank=share.bank, date_meeting=date.today())
    earning_share = EarningShare.objects.create(
        meeting=meeting, share=share, earning_by_share=10, total_earning_by_share=100, date_calculated=date.today())
    return earning_share


def bank_creation_data(
    city_id=0,
    bank_name=BANK_NAME_TEST,
    partners_guest=[
        {
            "name": PARTNER_GUEST_NAME_TEST,
            "phone_number": PARTNER_GUEST_PHONE_TEST,
            "phone_region_code": PHONE_REGION_CODE_TEST

        }
    ]
):
    return {
        "city": city_id,
        "name": bank_name,
        "partners": partners_guest
    }
