import os
import unittest
from credit_account import CreditAccount
from debit_account import DebitAccount
from hybrid_account import HybridAccount
from customer import Customer

os.environ["DATA_FILE"] = "test_data.json"

class TestBankApplication(unittest.TestCase):

    def setUp(self):
        self.credit_account = CreditAccount(1234, balance=0, credit_limit=500)
        self.debit_account = DebitAccount(2343, balance=100)
        self.hybrid_account = HybridAccount(5675, balance=50, credit_limit=300)
        self.customer = Customer(3454, "Arif")

    def test_credit_account_withdraw_limit(self):
        self.credit_account.withdraw(300)
        self.assertEqual(self.credit_account.balance, -300)

    def test_credit_account_exceed_limit(self):
        self.credit_account.withdraw(600)
        self.assertEqual(self.credit_account.balance, 0) 

    def test_debit_account_withdraw(self):
        self.debit_account.withdraw(50)
        self.assertEqual(self.debit_account.balance, 50)

    def test_debit_account_insufficient_funds(self):
        self.debit_account.withdraw(200)
        self.assertEqual(self.debit_account.balance, 100) 

    def test_hybrid_account_use_credit(self):
        self.hybrid_account.withdraw(200)  
        self.assertEqual(self.hybrid_account.balance, 0)
        self.assertEqual(self.hybrid_account.credit_limit, 150)

    def test_deposit(self):
        self.debit_account.deposite(100)
        self.assertEqual(self.debit_account.balance, 200)

    def test_customer_add_and_find_account(self):
        self.customer.add_account(self.credit_account)
        found_account = self.customer.find_account(1234)
        self.assertIsNotNone(found_account)
        self.assertEqual(found_account.account_number, 1234)

   
if __name__ == "__main__":
    unittest.main()