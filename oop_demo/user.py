class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f"{self.name}: {self.account_balance}")



mike = User("mike", "mike@email.com")
shelbi = User("shelbi", "shelbs@email.com")
ryan = User("ryan", "ryanf@email.com")

mike.make_deposit(50)
mike.make_deposit(150)
mike.make_deposit(250)
mike.make_withdrawal(100)
mike.display_user_balance()

shelbi.make_deposit(500)
shelbi.make_deposit(100)
shelbi.make_withdrawal(50)
shelbi.make_withdrawal(100)
shelbi.display_user_balance()

ryan.make_deposit(1000)
ryan.make_withdrawal(500)
ryan.make_withdrawal(100)
ryan.make_withdrawal(50)
ryan.display_user_balance()

