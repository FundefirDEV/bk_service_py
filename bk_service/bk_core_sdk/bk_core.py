
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
