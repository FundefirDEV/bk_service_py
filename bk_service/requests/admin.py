""" Requests models admin """

# Django
from django.contrib import admin

# Models
from bk_service.requests.models import *


@admin.register(ShareRequest)
class ShareRequestAdmin(admin.ModelAdmin):
    """ ShareRequest model admin """


@admin.register(CreditRequest)
class CreditRequestAdmin(admin.ModelAdmin):
    """ CreditRequest model admin """


@admin.register(PaymentScheduleRequest)
class PaymentScheduleRequestAdmin(admin.ModelAdmin):
    """ PaymentScheduleRequest model admin """
