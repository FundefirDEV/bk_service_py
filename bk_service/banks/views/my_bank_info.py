# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Models
from bk_service.banks.models import Credit

# Serializers
from bk_service.banks.serializers import CreditsModelSerializer

# Utils
from bk_service.utils.enums.banks import PaymentStatus


class MyBankInfoAPIView(APIView):
    def get(self, request, *args, **kwargs):

        partner = request.user.get_partner()
        credits = Credit.objects.filter(partner=partner, is_active=True)

        serializer = CreditsModelSerializer(credits, many=True)

        data = serializer.data

        # Return only schedule installments pending
        for credit_index, credit in enumerate(serializer.data):
            for schedule_installment_index, schedule_installment in enumerate(credit['schedule_installments']):

                if schedule_installment['payment_status'] is not str(PaymentStatus.pending):
                    data[credit_index]['schedule_installments'].pop(schedule_installment_index)

        return Response(serializer.data)
