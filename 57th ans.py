class student:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    def display(self):
        print(self.name)
        print(self.age)
n1 = student("ranjith", 27)
n2 = student ("arun",27)

n1.display()
n2.display()