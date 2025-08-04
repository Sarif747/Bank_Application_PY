from account import Account

class DebitAccount(Account):

    def withdraw(self,amount):
        if amount <= 0:
            print("Withdraw amount should be greater than 0")
            return False
        if amount > self.balance:
            print("Insufficient funds")
            return False
        self.balance = self.balance - amount
        print(f"Withdrawn: {amount}, New balance: {self.balance}")
