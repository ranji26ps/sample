class Bank:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print( self.balance)

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance")
        else:
            self.balance=self.balance-amount
            print(self.balance)

    def check_balance(self):
        print(self.balance)

b = Bank(123456, "John Doe", 500)
b.deposit(300)
b.withdraw(900)
b.check_balance()
