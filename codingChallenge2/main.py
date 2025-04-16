from dao.ILoanRepositoryImpl import ILoanRepositoryImpl
from entity import *
from exception import invalidOption
class LoanManagement():
    def __init__(self):
        self.processor=ILoanRepositoryImpl()
    def create_customer(self):
        if(True):
            try:
                name=input("Enter customer name :").strip()
                email=input("Enter email of customer :").strip()
                password=input("Enter the password (8 characters long):").strip()
                phone_number=input("Enter phone number :")
                address=input("Enter the address :")
                credit_score=int(input("Enter your credit score : "))
                id=self.processor.create_customer_login(name,email,password)
                customer=Customer(id,name,email,phone_number,address,credit_score)
                if(id!=None):
                    self.processor.create_customer(customer)
            except Exception as e:
                print("Error occured : ",e)
    def apply_loan(self):
        try:
            principal_amount=int(input("Enter the principal amount : "))
            interest_rate=int(input("enter the rate of intrest :"))
            loan_term=int(input("Enter the Loan term :"))
            loan_type=["Car Loan", "Home Loan"][int(input("Enter the loan type [Car Loan - 1 | Home Loan - 2] :"))-1]
            loan=Loan(None,None,principal_amount,interest_rate,loan_term,loan_type,"Pending")
            self.processor.applyLoan(loan)
        except Exception as e:
            print("Enter a valid data", e)
    def calculateInterest(self):
        loan_id=int(input("Enter the loan id :"))
        print("Intrest :",self.processor.calculateInterest(loan_id))
    def calculateEMI(self):
        loan_id=int(input("Enter the loan id :"))
        print("Intrest :",self.processor.calculateEMI(loan_id))
    def loanStatus(self):
        self.processor.loanStatus()
    def loanRepayment(self):
        loan_id=int(input("Enter the loan id :"))
        amount=int(input("Enter the amount :"))
        self.processor.loanRepayment(loan_id,amount)
    def getAllLoan(self):
        self.processor.getAllLoan()
    def getLoan(self):
        loan_id=int(input("Enter the loan id :"))
        self.processor.getLoanById(loan_id)
    def login(self):
        self.processor.login()
    def logout(self):
        self.processor.logout()
    def main(self):
        option=0
        while(option!=-1):
            try:
                print("\n1 -> Apply Loan")
                print("2 -> Get All Loans")
                print("3 -> Get Loan")
                print("4 -> Loan Repaymemnt")
                print("5 -> Create a Customer")
                print("6 -> Login")
                print("7 -> Logout")
                print("8 -> Exit")
                option=int(input("Enter the choice :"))
                if(option==1):
                    self.apply_loan()
                elif(option==2):
                    self.getAllLoan()
                elif(option==3):
                    self.getLoan()
                elif(option==4):
                    self.loanRepayment()
                elif(option==5):
                    self.create_customer()
                elif(option==6):
                    self.login()
                elif(option==7):
                    self.logout()
                elif(option==8):
                    print("bye bye")
                    return
                else:
                    raise invalidOption("\nError -> Invalid option. Please select a valid option\n")
            except invalidOption as e:
                print(e)
if __name__=="__main__":
    lm=LoanManagement()
    lm.main()