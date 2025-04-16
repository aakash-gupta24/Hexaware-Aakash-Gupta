class Loan:
    def __init__(self, loan_id, customer_id, principal_amount, interest_rate, loan_term, loan_type, loan_status):
        if  [loan_id, customer_id, principal_amount, interest_rate, loan_term, loan_type, loan_status].count(None)==7:
            self._loan_id = 0
            self._customer_id = 0
            self._principal_amount = 0.0
            self._interest_rate = 0.0
            self._loan_term = 0
            self._loan_type = ""
            self._loan_status = ""
        else:
            self._loan_id = loan_id
            self._customer_id = customer_id
            self._principal_amount = principal_amount
            self._interest_rate = interest_rate
            self._loan_term = loan_term
            self._loan_type = loan_type
            self._loan_status = loan_status

    def __str__(self):
        return (f"Loan[{self._loan_id}] for Customer[{self._customer_id}]: Amount: {self._principal_amount}, "f"Interest Rate: {self._interest_rate}, Loan Type: {self._loan_type}, Status: {self._loan_status}")

    def get_loan_id(self):
        return self._loan_id

    def set_loan_id(self, value):
        self._loan_id = value

    def get_customer_id(self):
        return self._customer_id

    def set_customer_id(self, value):
        self._customer_id = value

    def get_principal_amount(self):
        return self._principal_amount

    def set_principal_amount(self, value):
        self._principal_amount = value

    def get_interest_rate(self):
        return self._interest_rate

    def set_interest_rate(self, value):
        self._interest_rate = value

    def get_loan_term(self):
        return self._loan_term

    def set_loan_term(self, value):
        self._loan_term = value

    def get_loan_type(self):
        return self._loan_type

    def set_loan_type(self, value):
        self._loan_type = value

    def get_loan_status(self):
        return self._loan_status

    def set_loan_status(self, value):
        self._loan_status = value

__all__ = ['Loan']
