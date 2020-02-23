class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self 

    def display_user_balance(self):
        print(f"{self.name}: {self.account_balance}")
        return self

    def transfer_amount(self, target, amount):
        self.make_withdrawal(amount)
        target.make_deposit(amount)
        return self

class Bank_account:
    def __init__(self, account_balance=0):
        self.int_rate = 0.01
        self.balance = account_balance
        
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        self.balance += (1+self.int_rate) * self.balance
        return self
    
if __name__ == "__main__":
    Tanner = Bank_account(400).deposit(30).deposit(100).deposit(100).withdraw(100).yield_interest().display_account_info()
    Ryan = Bank_account(200).deposit(100).deposit(200).withdraw(100).withdraw(50).withdraw(100).withdraw(10).yield_interest().display_account_info()
    