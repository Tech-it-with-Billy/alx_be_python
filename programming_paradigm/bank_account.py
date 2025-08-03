class  BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance
        
    def deposit(self, amount):
        new_balance = self.account_balance + amount
        return new_balance
    
    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False
    
    def display_balance(self):
        return f'Current Balance: ${self.account_balance:.2f}'
    