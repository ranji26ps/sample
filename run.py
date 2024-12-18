class BankAccount:
    def __init__(self, account_holder, balance=0):
        
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        
        if amount > 0:
            self.balance += amount
            print("Deposited {amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance is ${self.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be greater than zero.")


account = BankAccount("John Doe", 1000)


account.deposit(500)


account.withdraw(200)


account.withdraw(2000)
