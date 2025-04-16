from .ILoanRepository import ILoanRepository
from util.DBPropertyUtil import DBPropertyUtil
from util.DBConnUtil import DBConnUtil
from exception.InvalidLoanException import InvalidLoanException
from exception.invalidOption import invalidOption
import math
class ILoanRepositoryImpl(ILoanRepository):
    def __init__(self):
        self.Logged_id=None
        self.conn_str = DBPropertyUtil.get_connection_string('db_config.properties')
        self.connection = DBConnUtil.get_connection(self.conn_str)

        if self.connection:
            self.cursor = self.connection.cursor()
    def create_customer_login(self,name,email,password):
        self.cursor.execute("select count(*) from loginCustomer where email=?",email)
        check=self.cursor.fetchone()
        if(check[0]==1):
            print(f"Customer already exist with email {email}")
            return None
        else:
            self.cursor.execute("insert into loginCustomer values(?,?,?)",name,email,password)
            self.connection.commit()
            self.cursor.execute("select customer_id from loginCustomer where email=?",email)
            return self.cursor.fetchone()[0]
        
    def create_customer(self,customer):
        self.cursor.execute("insert into Customer values(?,?,?,?,?)",customer.get_name(),customer.get_email_address(),customer.get_phone_number(),customer.get_address(),customer.get_credit_score())
        self.connection.commit()
        print("\nCustomer created successfully")

    def login(self):
        name=input("Enter the name :")
        pas=input("Enter the password :")
        self.cursor.execute("select count(*) from loginCustomer where name=? and password=?",name,pas)
        check=self.cursor.fetchone()
        if(check[0]==1):
            self.cursor.execute("select customer_id from loginCustomer where name=? and password=?",name,pas)
            self.Logged_id=self.cursor.fetchone()[0]
            print("\nLogged in\n")
    
    def logout(self):
        self.Logged_id=None
        print("\nLogged out\n")
    def applyLoan(self,loan):
        if(self.Logged_id==None):
            print("Login before applying for loan")
            self.login()
        if(self.Logged_id!=None):
            try:
                self.cursor.execute("insert into Loan values(?,?,?,?,?,?)",self.Logged_id,loan.get_principal_amount(),loan.get_interest_rate(),loan.get_loan_term(),loan.get_loan_type(),loan.get_loan_status())
                self.cursor.commit()
                print("Loan applied successfully")
                return 1
            except Exception as e:
                print(e)
    
    def calculateInterest(self,loan_id=None, principal_amount=None, interest_rate=None, loan_term=None):
        if loan_id is not None:
            self.cur.execute("select principal_amount, interest_rate, loan_term from Loan where loan_id = ?", loan_id)
            row = self.cursor.fetchone()        

            if not row:
                raise InvalidLoanException(f"Loan with ID {loan_id} not found.")

            principal_amount, interest_rate, loan_term = row

        if principal_amount is None or interest_rate is None or loan_term is None:
            raise ValueError("Missing parameters to calculate interest.")

        interest = (principal_amount * interest_rate * loan_term) / 12
        return interest
    
    def loanStatus(self,customer_id):
        if(customer_id==None):
            customer_id=self.Logged_id
        if(customer_id!=None):
            try:
                self.cursor.execute("select creditscore from Customer where customer_id=?",customer_id)
                credit_score=self.cursor.fetchone()[0]
                if(credit_score>650):
                    self.cursor.execute("update Loan set loan_status=? where customer_id=? and loan_status=?","Approved",customer_id,"Pending")
                    self.connection.commit()
                else:
                    self.cursor.execute("update Loan set loan_status=? where customer_id=? and loan_status=?","Rejected",customer_id,"Pending")
                    self.connection.commit()
            except Exception as e:
                print(e)

    def calculateEMI(self,loan_id=None, principal_amount=None, annual_interest_rate=None, loan_term=None):
        if loan_id is not None:
            self.cursor.execute("select principal_amount, interest_rate, loan_term from Loan where loan_id = ?", loan_id)
            row = self.cursor.fetchone()
            if not row:
                raise InvalidLoanException(f"Loan with ID {loan_id} not found.")

            principal_amount, annual_interest_rate, loan_term = row

        if principal_amount is None or annual_interest_rate is None or loan_term is None:
            raise ValueError("Missing parameters to calculate EMI.")

        monthly_interest_rate = annual_interest_rate / 12 / 100
        P = principal_amount
        R = monthly_interest_rate
        N = loan_term

        emi = (P * R * pow(1 + R, N)) / (pow(1 + R, N) - 1)
        return round(emi, 2)
    
    def loanRepayment(self,loan_id, amount):
        try:
            self.cursor.execute("select principal_amount, interest_rate, loan_term from Loan where loan_id = ?", loan_id)
            row = self.cursor.fetchone()

            if not row:
                raise InvalidLoanException(f"Loan with ID {loan_id} not found.")

            principal_amount, annual_interest_rate, loan_term = row

            monthly_interest_rate = annual_interest_rate / 12 / 100
            P = principal_amount
            R = monthly_interest_rate
            N = loan_term

            emi = (P * R * pow(1 + R, N)) / (pow(1 + R, N) - 1)
            emi = round(emi, 2)

            if amount < emi:
                print(f"Payment rejected. Amount {amount} is less than EMI {emi}.")
                return

            no_of_emis_paid = math.floor(amount / emi)
            total_paid = round(no_of_emis_paid * emi, 2)
            new_principal = round(principal_amount - total_paid, 2)
            if(new_principal<0):
                print(f"Amount {total_paid-principal_amount} extra paid. ")
                new_principal=0
            self.cursor.execute("update Loan set principal_amount = ? where loan_id = ?", new_principal, loan_id)
            self.connection.commit()

            print(f"Payment of {amount} accepted.")
            print(f"{no_of_emis_paid} EMIs paid. Remaining principal: {new_principal}.")
            return 1

        except InvalidLoanException as e:
            print(e)

        except Exception as ex:
            print("Error:", ex)

    def getAllLoan(self):
        try:
            customer_no=1
            self.cursor.execute("select * from Customer")
            customer_details=self.cursor.fetchall()
            for row1 in customer_details:
                self.loanStatus(row1.customer_id,)
                print(f"\n=========== Customer {customer_no}===========")
                customerd={
                    "Customer ID": row1.customer_id,
                    "Name":row1.name,
                    "Email":row1.email_address,
                    "Phone Number":row1.phone_number,
                    "Address":row1.address,
                    "Credit Score":row1.creditscore
                }
                for key, value in customerd.items():
                    print(f"{key}: {value}")

                self.cursor.execute("select * from Loan where customer_id=?",row1.customer_id)
                loans = self.cursor.fetchall()

                if not loans:
                    print(f"----- Cutomer {customer_no} Loan Details -----")
                    customer_no+=1
                    print("No loans found.")
                    print("\n=============================\n")
                    continue
                loan_list = []

                print(f"\n----- Cutomer {customer_no} Loan Details -----\n")
                for row in loans:
                    loan = {
                        "Loan ID": row.loan_id,
                        "Customer ID": row.customer_id,
                        "Principal Amount": row.principal_amount,
                        "Interest Rate": row.interest_rate,
                        "Loan Term": row.loan_term,
                        "Loan Type": row.loan_type,
                        "Loan Status": row.loan_status
                    }
                    loan_list.append(loan)

                    for key, value in loan.items():
                        print(f"{key}: {value}")
                    print("\n-----------------------------\n")
                print("=============================\n")
                customer_no+=1

            return  []

        except Exception as e:
            print("Error fetching loans:", e)
            return []
    
    def getLoanById(self,loan_id):
        try:
            customer_id=None
            self.cursor.execute("select customer_id from Loan where loan_id=?",loan_id)
            customer_id=self.cursor.fetchone()[0]
            self.loanStatus(customer_id)
            self.cursor.execute("select * from Customer where customer_id=?",customer_id)
            customer_details=self.cursor.fetchone()
            print("=========== Customer Details ===========")
            print("Customer ID :",customer_details[0])
            print("Name :",customer_details[1])
            print("Email :",customer_details[2])
            print("Phone Number :",customer_details[3])
            print("Address :",customer_details[4])
            print("Credit Score :",customer_details[5])
            print("-----------------------------")
            self.cursor.execute("select * FROM Loan where loan_id=?",loan_id)
            loans = self.cursor.fetchall()

            if not loans:
                print("No loans found.")
                return []

            loan_list = []

            print("----- Loan Details -----")
            for row in loans:
                loan = {
                    "Loan ID": row.loan_id,
                    "Customer ID": row.customer_id,
                    "Principal Amount": row.principal_amount,
                    "Interest Rate": row.interest_rate,
                    "Loan Term": row.loan_term,
                    "Loan Type": row.loan_type,
                    "Loan Status": row.loan_status
                }
                loan_list.append(loan)

                for key, value in loan.items():
                    print(f"{key}: {value}")
                print("-----------------------------")
            print("=============================\n")
            return 1

        except Exception as e:
            print("Error fetching loans:", e)
            return []
