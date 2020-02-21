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



mike = User("mike", "mike@email.com")
shelbi = User("shelbi", "shelbs@email.com")
ryan = User("ryan", "ryanf@email.com")

mike.make_deposit(50).make_deposit(150).make_deposit(250).make_withdrawal(100).display_user_balance().transfer_amount(shelbi, 50).display_user_balance()

shelbi.make_deposit(500).make_deposit(100).make_withdrawal(50).make_withdrawal(100).display_user_balance().display_user_balance()

ryan.make_deposit(1000).make_withdrawal(500).make_withdrawal(100).make_withdrawal(50).display_user_balance()