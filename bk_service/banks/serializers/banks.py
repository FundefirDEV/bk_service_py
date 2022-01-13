""" Bank serializers """

# Django

# Django REST Framework
from rest_framework import serializers

# Models
from bk_service.banks.models import Bank, Partner
from bk_service.banks.models.partners_guest import PartnerGuest
from bk_service.banks.models.partners import Partner, PartnerDetail
from bk_service.banks.models.bank_rules import BankRules

# Utils Errors
from bk_service.utils.constants_errors import build_error_message
from bk_service.utils.constants_errors import *

# Utils enums
from bk_service.utils.enums.banks import PartnerType
from bk_service.utils.bank_rules_constants import BankRulesConstants

# import pdb


class BankModelSerializer(serializers.ModelSerializer):
    """ Bank model serializers """
    class Meta:
        model = Bank
        fields = ('name', 'city', 'cash_balance', 'active_credits', 'shares',
                  'expense_fund', 'bad_debt_reserve', )

        extra_kwargs = {
            'name': {
                "error_messages": {
                    'required': build_error_message(BANK_NAME_REQUIRED),
                    'invalid': build_error_message(BANK_NAME_INVALID),
                    'unique': build_error_message(BANK_NAME_EXIST),
                },
            },
            'city': {
                "error_messages": {
                    'required': build_error_message(CITY_REQUIRED),
                    'invalid': build_error_message(CITY_INVALID),
                    'does_not_exist': build_error_message(CITY_INVALID)
                }
            },
        }

    def create(self, name, city, partners, user, ):

        bank = Bank.objects.create(name=name, city=city)

        # Set User City
        user.city = city
        user.save()

        partner_creator = self.insert_partner_creator(bank=bank, user=user)
        partners_guests = self.insert_partners_guest(bank=bank, partners=partners)

        return bank

    def insert_partner_creator(self, bank, user):
        partner_creator = Partner.objects.create(
            user=user,
            bank=bank,
            is_creator=True,
            is_active=True,
            phone_number=user.phone_number,
            phone_region_code=user.phone_region_code,
            role=PartnerType.admin,
        )

        return partner_creator

    def insert_partners_guest(self, bank, partners):

        partner_guest_list = []

        for partner in partners:
            partner_guest_list.append(PartnerGuest(
                name=partner['name'],
                phone_number=partner['phone_number'],
                phone_region_code=partner['phone_region_code'],
                bank=bank,
            ))

        return PartnerGuest.objects.bulk_create(partner_guest_list)


class CreateBankPartnersSerializer(serializers.ModelSerializer):
    """ Create Bank partners serializers """

    class Meta:
        model = PartnerGuest
        fields = ('name', 'phone_number', 'phone_region_code', )

        extra_kwargs = {
            'phone_number': {
                "error_messages": {
                    'required': build_error_message(PARTNER_GUEST_PHONE_REQUIRED),
                    'unique': build_error_message(PARTNER_GUEST_PHONE_EXIST),
                    'invalid': build_error_message(PARTNER_GUEST_PHONE_INVALID),
                }
            },
            'name': {
                "error_messages": {
                    'required': build_error_message(USERNAME_REQUIRED),
                    'invalid': build_error_message(USERNAME_INVALID),
                },
            },
            'phone_region_code': {
                "error_messages": {
                    'required': build_error_message(PHONE_REGION_CODE_REQUIRED),
                    'invalid': build_error_message(PHONE_REGION_CODE_INVALID),
                }
            },
        }


class CreateBankSerializer(serializers.Serializer):
    """ Create Bank serializers """

    partners = CreateBankPartnersSerializer(many=True)

    name = serializers.CharField(
        min_length=4,
        max_length=64,
        required=True,
        error_messages={
            'required': build_error_message(BANK_NAME_REQUIRED),
            'invalid': build_error_message(BANK_NAME_INVALID),
            'unique': build_error_message(BANK_NAME_EXIST),
        },
    )

    city = serializers.IntegerField(
        required=True,
        error_messages={
            'required': build_error_message(CITY_REQUIRED),
            'invalid': build_error_message(CITY_INVALID),
            'does_not_exist': build_error_message(CITY_INVALID)
        },
    )
