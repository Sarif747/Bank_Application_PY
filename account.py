class Account():

    def __init__(self,account_number,balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposite(self,amount):
        if amount <= 0:
            print("Depsosite ammount is invalid")
            return
        elif amount == 0:
            print("Deposite ammount must be greater than 0")
            return
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    
    def check_balance(self):
        print(f"Account {self.account_number}, balance: {self.balance}")
        return self.balance
    
    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "account_number": self.account_number,
            "balance": self.balance
        }
    

         

        