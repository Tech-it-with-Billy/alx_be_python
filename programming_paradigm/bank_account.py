#
    
    
    
    # bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.account_balance = initial_balance  # private attribute

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
