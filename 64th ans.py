class person:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    def display(self):
        print(self.name)
        print(self.age)
ss = person("hello my name is ranjith", "iam 26 years old")
ss.display()
