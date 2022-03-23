# Django

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from bk_service.banks.models import PaymentSchedule

# Serializer
from bk_service.banks.serializers.partners import PartnerModelSerializer


class PaymentScheduleModelSerializer(serializers.ModelSerializer):
    """ Payment Schedule Model serializers """

    partner = PartnerModelSerializer(read_only=True)

    class Meta:
        model = PaymentSchedule
        fields = (
            'id',
            'bank',
            'partner',
            'payment_schedule_request',
            'amount',
            'ordinary_interest_paid',
            'capital_paid',
            'delay_interest_paid',
            'payment_type',
            'created_at',
        )
