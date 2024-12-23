class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        
            return self.num1 / self.num2
       
num1 =int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

abc = Calculator(num1, num2)

print("The sum of ", abc.add())
print("The difference of",abc.subtract())
print("The product of ", abc.multiply())
print("The division of 0", abc.divide())
