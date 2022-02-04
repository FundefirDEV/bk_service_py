# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Django
from django.db.models import Sum

# Models
from bk_service.banks.models import Credit, PaymentSchedule, Meeting

# Serializers
from bk_service.banks.serializers import CreditsModelSerializer, PaymentScheduleModelSerializer

# Utils enums
from bk_service.utils.enums.requests import CreditPayType


class CreditsCurrentMeetingAPIView(APIView):
    def get(self, request, *args, **kwargs):

        partner = request.user.get_partner()
        credits = Credit.objects.filter(is_active=True, meeting=None, bank=partner.bank)
        payment_schedules = PaymentSchedule.objects.filter(meeting=None, bank=partner.bank)

        credit_serializer = CreditsModelSerializer(credits, many=True)
        payment_schedules_serializer = PaymentScheduleModelSerializer(payment_schedules, many=True)

        res = {
            'partnerts_credits': credit_serializer.data,
            'partnerts_payments_schedule': payment_schedules_serializer.data
        }

        return Response(res)
