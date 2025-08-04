import random

from credit_account import CreditAccount
from customer import Customer
from debit_account import DebitAccount
from hybrid_account import HybridAccount
from storage import load_data, save_data

# method to generate randon customer id
def generate_random_id(existing_customers):
    existing_ids = {c.customer_id for c in existing_customers}
    attempts = 0
    while attempts < 10000:  
        rand_id = random.randint(1000, 9999)
        if rand_id not in existing_ids:
            return rand_id
        attempts += 1
    raise Exception("Unable to generate unique 4-digit ID. All possible IDs might be used.")

# method to generate random account numbers
def generate_random_accountno(customer):
    existing_account_nos = {acc.account_number for acc in customer.accounts}
    attempts = 0
    while attempts < 10000:
        rand_no = random.randint(1000, 9999)
        if rand_no not in existing_account_nos:
            return rand_no
        attempts += 1
    raise Exception("Unable to generate unique 4-digit account number.")

#  method to create customer with customer_id and name
def create_customer(customers):
    name = input("Enter customer name:")
    customer_id = generate_random_id(customers)
    customer = Customer(customer_id, name)
    customers.append(customer)
    print(f"Customer created with id: {customer_id}")

#  method to create account 
def create_account(customers):
    customer_id = input("Enter customer id:")
    customer = find_customer(customers,customer_id)
    if not customer:
        print("Customer not found")
        return
    print("1. Credit Account\n2. Deposite Account\n3. Hybrid Account")
    choice = input("Enter type of account choice:")
    account_number = generate_random_accountno(customer)
    if choice == "1":
        account = CreditAccount(account_number)
    elif choice == "2":
        account = DebitAccount(account_number)
    elif choice == "3":
        account = HybridAccount(account_number)
    else:
        print("Invalid Choice")
        return
    customer.add_account(account)
    print(f"Account created with account number: {account.account_number}")
    2

#  method to find customer details
def find_customer(customers,customer_id):
    for customer in customers:
        print(customer.customer_id == int(customer_id))
        if customer.customer_id == int(customer_id):
            return customer

#  method to find acount details using customer id or account number
def search_account_customer(customers):
    search_id = input("Enter the customer ID or Account number:")
    for customer in customers:
        if customer.customer_id == int(search_id):
            print(f"Customer: {customer.name}, ID: {customer.customer_id}")
            for account in customer.accounts:
                account.check_balance()
            return
        for account in customer.accounts:
            if account.account_number == int(search_id):
                print(f'Account found under customer name: {customer.name}')
                account.check_balance()
                return
    print("Not Found")

#  method to do withdraw, deposite and check balance operation
def transaction(customers):
    account_number = input("Enter the account number:")
    for customer in customers:
        account = customer.find_account(int(account_number))
        if account:
            print("1. Deposite\n2. Withdraw\n3. Check Balance")
            choice = input("Enter any choice of transaction:")
            if choice == "1":
                amount = input("Enter ammount:")
                account.deposite(int(amount))
            elif choice == "2":
                amount = input("Enter amount:")
                account.withdraw(int(amount))
            elif choice == "3":
                account.check_balance()
            return
    print("Account Not Found")

#  main method where user can select the choice of operation they want to perform
def main():
    customers = load_data()
    for customer in customers:
        print(type(customer.customer_id))
    while True:
        print("________Bank menu________")
        print("1. Create Customer")
        print("2. Create Account")
        print("3. Search Customer/Account")
        print("4. Transaction")
        print("5. Exit")
        choice = input("Enter choice:")
        if choice == "1":
            create_customer(customers)
            save_data(customers)
        elif choice == "2":
            create_account(customers)
            save_data(customers)
        elif choice == "3":
            search_account_customer(customers)
            save_data(customers)
        elif choice == "4":
            transaction(customers)
            save_data(customers)
        elif choice == "5":
            save_data(customers)
            print("Data Saved")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()