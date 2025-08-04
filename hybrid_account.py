from account import Account

class HybridAccount(Account):

    def __init__(self,account_number,balance=0,credit_limit=1000):
        super().__init__(account_number,balance)
        self.credit_limit = credit_limit

    def withdraw(self,amount):
        if amount == 0:
            print("Withdraw ammount should be greater than 0")
            return
        elif self.balance >= amount:
            self.balance = self.balance - amount
            print(f"Withdraw amount {amount}, New balance: {self.balance}")
        elif (self.balance + self.credit_limit) >= amount:
            remaining = amount - self.balance
            self.balance = 0
            self.credit_limit = self.credit_limit - remaining
            print(f"Used hybrid account {self.account_number}, Remainig credit: {self.credit_limit}")
        else:
            print("Not enough funds or credit.")

    def to_dict(self):
        data = super().to_dict()
        data["credit_limit"] = self.credit_limit
        return data