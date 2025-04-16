class Customer:
    def __init__(self, customer_id, name, email_address, phone_number, address, credit_score):
        if customer_id is None:
            self._customer_id = 0
            self._name = ""
            self._email_address = ""
            self._phone_number = ""
            self._address = ""
            self._credit_score = 0
        else:
            self._customer_id = customer_id
            self._name = name
            self._email_address = email_address
            self._phone_number = phone_number
            self._address = address
            self._credit_score = credit_score

    def __str__(self):
        return f"Customer[{self._customer_id}] - {self._name}, {self._email_address}, {self._phone_number}"

    def get_customer_id(self):
        return self._customer_id

    def set_customer_id(self, value):
        self._customer_id = value

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_email_address(self):
        return self._email_address

    def set_email_address(self, value):
        self._email_address = value

    def get_phone_number(self):
        return self._phone_number

    def set_phone_number(self, value):
        self._phone_number = value

    def get_address(self):
        return self._address

    def set_address(self, value):
        self._address = value

    def get_credit_score(self):
        return self._credit_score

    def set_credit_score(self, value):
        self._credit_score = value


__all__=['Customer']