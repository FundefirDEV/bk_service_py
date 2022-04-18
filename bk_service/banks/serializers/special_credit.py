""" Special Credit serializers """

# Django

# Django REST Framework
from rest_framework import serializers

# Models
from bk_service.banks.models import Credit


class SpecialCreditSerializer(serializers.Serializer):
    """ Create special credit serializers """
    delay_interest = serializers.IntegerField(required=True, min_value=0, max_value=100)
    ordinary_interest = serializers.IntegerField(required=True, min_value=0, max_value=100)
    installments = serializers.IntegerField(required=True, min_value=1, max_value=100)
    payment_period_of_installments = serializers.IntegerField(required=True, min_value=1, max_value=160)
    amount = serializers.IntegerField(required=True, min_value=1)
    credit_use = serializers.CharField(required=True)
    credit_use_detail = serializers.CharField(required=True)
    payment_type = serializers.CharField(required=True)
    partner_id = serializers.IntegerField(required=True)
