""" Bank models admin """

# Django
from django.contrib import admin

# Models
from bk_service.banks.models import *


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    """ Partner model admin """
    list_display = ('user',  'bank')
    # fields = ('name', 'city', 'cash_balance', 'active_credits',
    #           'shares', 'expenditure_fund', 'reserve_fund_of_bad_debt')
    search_fields = ('user',)
    list_filter = ('bank__name', 'user__city')


@admin.register(PartnerDetail)
class PartnerDetailAdmin(admin.ModelAdmin):
    """ PartnerDetail model admin """
    list_display = ('partner',)
    # fields = ('name', 'city', 'cash_balance', 'active_credits',
    #           'shares', 'expenditure_fund', 'reserve_fund_of_bad_debt')
    search_fields = ('partner',)
    # list_filter = ('bank__name', 'user__city')


@admin.register(PartnerGuest)
class PartnerAdmin(admin.ModelAdmin):
    """ Partner guest model admin """
    # list_display = '__all__'
    # search_fields = ('name', 'code',)
    # list_filter = ('is_active', 'name', 'code',)


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    """ Bank model admin """

    list_display = ('name', 'city',)
    fields = ('name', 'city', 'cash_balance', 'active_credits',
              'shares', 'expenditure_fund', 'reserve_fund_of_bad_debt')
    search_fields = ('name',)
    list_filter = ('name', 'city')


# @admin.register(BankRules)
# class BankRulesAdmin(admin.ModelAdmin):
#     """ BankRules model admin """
#     # list_display = '__all__'
#     # search_fields = ('name', 'code',)
#     # list_filter = ('is_active', 'name', 'code',)


@admin.register(Share)
class ShareAdmin(admin.ModelAdmin):
    """ Share model admin """
    # list_display = '__all__'
    # search_fields = ('name', 'code',)
    # list_filter = ('is_active', 'name', 'code',)


@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    """ Credit model admin """
    # list_display = '__all__'
    # search_fields = ('name', 'code',)
    # list_filter = ('is_active', 'name', 'code',)


@admin.register(PaymentSchedule)
class PaymentScheduleAdmin(admin.ModelAdmin):
    """ PaymentSchedule model admin """
    # list_display = '__all__'
    # search_fields = ('name', 'code',)
    # list_filter = ('is_active', 'name', 'code',)


@admin.register(ScheduleInstallment)
class ScheduleInstallmentAdmin(admin.ModelAdmin):
    """ ScheduleInstallment model admin """
    # list_display = '__all__'
    # search_fields = ('name', 'code',)
    # list_filter = ('is_active', 'name', 'code',)


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    """ Meeting model admin """
    list_display = (
        'bank',
        'close_date',
        'close_date',
    )
    fields = ('bank',
              'total_shares_amount',
              'total_credits_amount',
              'total_shares_quantity',
              'total_credits_quantity',
              'total_ordinary_interest',
              'total_capital',
              'earning_by_share',
              'total_delay_interest',
              'expenditure_fund',
              'reserve_fund_of_bad_debt',
              'close_date',
              )
    search_fields = ('bank__name',)
    list_filter = ('bank__name', 'created_at', 'updated_at')


@admin.register(EarningShare)
class EarningShareAdmin(admin.ModelAdmin):
    """ EarningShare model admin """
    # list_display = '__all__'
    # search_fields = ('name', 'code',)
    # list_filter = ('is_active', 'name', 'code',)
