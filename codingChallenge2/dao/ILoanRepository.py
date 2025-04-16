from abc import ABC , abstractmethod

class ILoanRepository(ABC):
    @abstractmethod
    def applyLoan(self,loan):
        pass

    @abstractmethod
    def loanStatus(self,loan_id):
        pass

    @abstractmethod
    def calculateEMI(self,loan_id=None, principal_amount=None, annual_interest_rate=None, loan_term=None):
        pass

    @abstractmethod
    def loanRepayment(self,loadn_id,amount):
        pass

    @abstractmethod
    def getAllLoan(self):
        pass

    @abstractmethod
    def getLoanById(seld,loan_id):
        pass
    @abstractmethod
    def loanRepayment(self,loan_id, amount):
        pass
    @abstractmethod
    def create_customer_login(self,name,email,password):
        pass

    @abstractmethod
    def create_customer(self,customer):
        pass

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass
    @abstractmethod
    def calculateInterest(self,loan_id=None, principal_amount=None, interest_rate=None, loan_term=None):
        pass
