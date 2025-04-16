from .Loan import Loan 

class CarLoan(Loan):
    def __init__(self, loan_id, customer_id, principal_amount, interest_rate, loan_term,loan_status, car_model, car_value):
        if loan_id is None:
            super().__init__()
            self._car_model = ""
            self._car_value = 0
        else:
            super().__init__(loan_id, customer_id, principal_amount, interest_rate, loan_term, "Car Loan", loan_status)
            self._car_model = car_model
            self._car_value = car_value

    def get_car_model(self):
        return self._car_model

    def set_car_model(self, value):
        self._car_model = value

    def get_car_value(self):
        return self._car_value

    def set_car_value(self, value):
        self._car_value = value

    def __str__(self):
        return (super().__str__() + f", Car Model: {self._car_model}, Car Value: {self._car_value}")

__all__=['CarLoan']