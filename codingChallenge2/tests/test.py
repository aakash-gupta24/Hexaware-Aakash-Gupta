import unittest
from unittest.mock import patch
from util.DBPropertyUtil import DBPropertyUtil
from util.DBConnUtil import DBConnUtil
from entity import *
from dao.ILoanRepositoryImpl import ILoanRepositoryImpl
class Tesing(unittest.TestCase):
    def setUp(self):
        self.conn_str = DBPropertyUtil.get_connection_string('db_config.properties')
        self.connection = DBConnUtil.get_connection(self.conn_str)
        self.processor=ILoanRepositoryImpl()
    def test_apply_loan(self):
        with patch('builtins.input', side_effect=[ 100,10,6,1,"ag","qwe123qwe"]):
            principal_amount=int(input("Enter the principal amount : "))
            interest_rate=int(input("enter the rate of intrest :"))
            loan_term=int(input("Enter the Loan term :"))
            loan_type=["Car Loan", "Home Loan"][int(input("Enter the loan type [Car Loan - 1 | Home Loan - 2] :"))-1]
            loan=Loan(None,None,principal_amount,interest_rate,loan_term,loan_type,"Pending")
            self.assertTrue(self.processor.applyLoan(loan),msg="Failed to apply loan")
    def test_get_loan_by_id(self):
        with patch('builtins.input', side_effect=[1]):
            loan_id=int(input("Enter loan Id : "))
            self.processor.getLoanById(loan_id)
    
    def test_loan_repayment(self):
        with patch('builtins.input', side_effect=[2,100]):
            loan_id=int(input("Enter loan Id : "))
            amount=int(input("Enter the amount : "))
            self.processor.loanRepayment(loan_id,amount)
    