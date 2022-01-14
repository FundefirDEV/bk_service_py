
class BkCore():

    def maximun_number_of_shares(self, total_shares, maximum_shares_percentage):
        return (total_shares * maximum_shares_percentage)/100

    def calculate_share_amount(self, shares_quantity, share_value):
        return (shares_quantity * share_value)

    def calculate_partner_maximun_credit_request(self, total_shares_amount, credit_investment_relationship):
        return (total_shares_amount * credit_investment_relationship)
