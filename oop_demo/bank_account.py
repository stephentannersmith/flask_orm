class BankAccount:
    def __init__(self, starting_balance=0):
        self.int_rate = 0.01
        self.balance = starting_balance
        
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Not enough moolah: You're outty $5")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        self.balance += (1+self.int_rate) * self.balance
        return self

class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount()

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self 

    def display_user_info(self):
        print(f"{self.name}: {self.account.balance}")
        return self

    def transfer_amount(self, target, amount):
        self.make_withdrawal(amount)
        target.make_deposit(amount)
        return self
    
if __name__ == "__main__":
    Tanner = BankAccount(400).deposit(30).deposit(100).deposit(100).withdraw(100).yield_interest().deposit(1000).display_account_info()
    Ryan = BankAccount(200).deposit(100).deposit(200).withdraw(100).withdraw(50).withdraw(100).withdraw(10).yield_interest().display_account_info()
