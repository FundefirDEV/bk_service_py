
# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
# Models
from bk_service.banks.models import Partner, PartnerDetail
# Enums
from bk_service.utils.enums.banks import PartnerType
# Serializer
from bk_service.banks.serializers.partner_admin import PartnersAdminSerializer
# Errors
from bk_service.utils.constants_errors import build_error_message
from bk_service.utils.exceptions_errors import CustomException
from bk_service.utils.constants_errors import PARTNER_IS_NOT_ADMIN


class PartnerAdminApiView(APIView):
    def post(self, request, *args, **kwargs):
        partner = request.user.get_partner()
        bank = partner.bank
        if partner.role != PartnerType.admin:
            raise CustomException(error=PARTNER_IS_NOT_ADMIN)
        data = request.data
        serializer = PartnersAdminSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        response_data = serializer.data

        for valid_data in response_data:
            # import pdb
            # pdb.set_trace()
            PartnersAdminSerializer.update_admin(
                partner_id=valid_data['id'],
                role=valid_data['role'],
                bank=bank)

        return Response('ok')
