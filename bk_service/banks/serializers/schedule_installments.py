""" Schedule Installmet serializers """

# Django

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from bk_service.banks.models import ScheduleInstallment


class ScheduleInstallmentModelSerializer(serializers.ModelSerializer):
    """ Schedule Installment model serializers """

    class Meta:
        model = ScheduleInstallment
        fields = (
            'id',
            'credit',
            'capital_installment',
            'payment_date',
            'ordinary_interest_percentage',
            'ordinary_interest_calculated',
            'total_pay_installment',
            'payment_status',
            'amount_paid',
            'capital_paid',
            'ordinary_interest_paid',
            'delay_interest_paid',
            'installment_number',
        )
