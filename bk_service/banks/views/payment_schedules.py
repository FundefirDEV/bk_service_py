# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Models
from bk_service.banks.models import PaymentSchedule

# Serializers
from bk_service.banks.serializers import PaymentScheduleModelSerializer


class PaymentScheduleModelAPIView(APIView):
    def get(self, request, *args, **kwargs):

        partner = request.user.get_partner()
        paymentSchedule = PaymentSchedule.objects.filter(bank=partner.bank, partner=partner)
        serializer = PaymentScheduleModelSerializer(paymentSchedule, many=True)

        return Response(serializer.data)
