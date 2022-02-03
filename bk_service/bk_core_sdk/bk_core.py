
# math
import math

# datetime
from datetime import datetime, timedelta
# enum
from bk_service.utils.enums import CreditPayType


class BkCore():

    def maximun_number_of_shares(self, total_shares, maximum_shares_percentage):
        return (total_shares * maximum_shares_percentage)/100

    def calculate_share_amount(self, shares_quantity, share_value):
        return (shares_quantity * share_value)

    def calculate_partner_maximun_credit_request(self, total_shares_amount, credit_investment_relationship):
        return (total_shares_amount * credit_investment_relationship)

    def calculate_credit_total_interest(self, amount, ordinary_interest, installments):
        return (amount * (ordinary_interest / 100)) * installments

    def calculate_expenditure_fund(self, total_interest, expenditure_fund_percentage):
        return total_interest * (expenditure_fund_percentage / 100)

    def calculate_reserve_fund_of_bad_debt(self, total_interest, reserve_fund_of_bad_debt_percentage):
        return total_interest * (reserve_fund_of_bad_debt_percentage / 100)

    def calculate_total_earning(self, total_interest, expenditure_fund, reserve_fund_of_bad_debt):

        if total_interest <= 0:
            return 0

        return total_interest - expenditure_fund - reserve_fund_of_bad_debt

    def calculate_earning_by_share(self, total_earning, bank_shares_quantity):

        if bank_shares_quantity <= 0:
            return 0

        return (total_earning / bank_shares_quantity)

    def calculate_schedule_installment(self, installments, payment_type, ordinary_interest, credit_amount, payment_period_of_installment):

        if payment_type == CreditPayType.installments:
            total_ordinary_interest = self.calculate_credit_total_interest(
                amount=credit_amount, installments=installments, ordinary_interest=ordinary_interest)
        if payment_type == CreditPayType.advance:
            total_ordinary_interest = 0

        total_credit_value = credit_amount + total_ordinary_interest
        installment_int_value, installment_dec_value = divmod(total_credit_value, installments)

        # installment_value, installment_ordinary_interest, instalment_capital_value
        schedules_installments = []

        ordinary_interest_per_installment_int, ordinary_interest_per_installment_dec = divmod(
            total_ordinary_interest, installments)

        today = datetime.now()
        for i in range(0, installments):
            # the first installment it's going to get the decimal part
            if i == 0:
                installment_value = installment_int_value + installment_dec_value
                installment_ordinary_interest = ordinary_interest_per_installment_int + ordinary_interest_per_installment_dec

            else:
                installment_value = installment_int_value
                installment_ordinary_interest = ordinary_interest_per_installment_int

            # days_to_pay = bank_rules.payment_period_of_installment * installment_number
            days_to_pay = payment_period_of_installment * (i+1)
            installment_payment_date = today + timedelta(days=days_to_pay)

            schedules_installments.append({'installment_value': installment_value,
                                           'ordinary_insterest': installment_ordinary_interest,
                                           'capital_value': installment_value - installment_ordinary_interest,
                                           'installment_payment_date': installment_payment_date})
        return schedules_installments

    def calculate_ordinary_interest_paid(
        self,
        amount_paid,
        payment_schedule_request_amount,
        schedule_installment_interest,
        is_payment_advance,
    ):

        if is_payment_advance:
            return 0.0

        ordinary_interest_paid = 0.0

        if(amount_paid >= schedule_installment_interest):
            ordinary_interest_paid = 0.0
        else:
            pending_interest = schedule_installment_interest - amount_paid

            if(payment_schedule_request_amount >= pending_interest):
                ordinary_interest_paid = pending_interest
            else:
                ordinary_interest_paid = payment_schedule_request_amount

        return ordinary_interest_paid
