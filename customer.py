from credit_account import CreditAccount
from debit_account import DebitAccount
from hybrid_account import HybridAccount

class Customer():

    def __init__(self,customer_id,name):
        self.customer_id = customer_id
        self.name = name
        self.accounts = []

    def add_account(self,account):
        self.accounts.append(account)
    
    def find_account(self,account_number):
        for acc in self.accounts:
            if acc.account_number == account_number:
                return acc
            return None
        
    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "accounts": [acc.to_dict() for acc in self.accounts]
        }

    @staticmethod
    def from_dict(data):
        customer = Customer(data["customer_id"], data["name"])
        for acc_data in data["accounts"]:
            acc_type = acc_data["type"]
            if acc_type == "CreditAccount":
                account = CreditAccount(acc_data["account_number"],acc_data['balance'],acc_data.get('credit_limit',1000))
            elif acc_type == "DebitAccount":
                account = CreditAccount(acc_data["account_number"],acc_data['balance'])
            elif acc_type == "HybridAccount":
                account = CreditAccount(acc_data["account_number"],acc_data['balance'],acc_data.get('credit_limit',1000))
            else:
                print("Unknown account type") 
            customer.add_account(account)   
        return customer