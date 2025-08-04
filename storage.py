import json
import os
from credit_account import CreditAccount
from customer import Customer
from debit_account import DebitAccount
from hybrid_account import HybridAccount

DATA_FILE = "data.json"

def save_data(customers):
    data = [customer.to_dict() for customer in customers]
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    if os.path.getsize(DATA_FILE) == 0:
        return []  
    with open(DATA_FILE, "r") as f:
        try:
            data = json.load(f)
            return [Customer.from_dict(c) for c in data]
        except json.JSONDecodeError:
            print("Warning: Invalid JSON format in data file.")
            return []

