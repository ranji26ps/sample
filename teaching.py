class Bank_holder():
    def __init__(self,ah,bm,):
        self.acount_holder = ah
        self.bank_methord = bm
        self.balance = 0
    def deposit(self,a):
        if a > 0:
            self.balance = self.balance+a
            print(self.balance)
    def withdraw (self,a):
        if self.balance > a:
           self.balance = self.balance - a
           print(self.balance)
        else:
            print("Insufficient funds")
a1 = Bank_holder("Ranjith","saving")
a1.deposit(444)
a1.withdraw(500)
                    