from .Loan import Loan 

class HomeLoan(Loan):
    def __init__(self, loan_id, customer_id, principal_amount, interest_rate, loan_term,loan_status, property_address, property_value):
        if loan_id is None:
            super().__init__()
            self._property_address = ""
            self._property_value = 0
        else:
            super().__init__(loan_id, customer_id, principal_amount, interest_rate, loan_term, "Home Loan", loan_status)
            self._property_address = property_address
            self._property_value = property_value
            
    def __str__(self):
        return (super().__str__() + f", Property Address: {self._property_address}, Property Value: {self._property_value}")

    def get_property_address(self):
        return self._property_address

    def set_property_address(self, value):
        self._property_address = value

    def get_property_value(self):
        return self._property_value

    def set_property_value(self, value):
        self._property_value = value

__all__=['HomeLoan']