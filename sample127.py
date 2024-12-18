class car:
    def __init__(self,m,mn,y,e):
        self.manufacture = m
        self.model = mn
        self.year = y
        self.e = e
    def display(self):
        print(self.manufacture)
        print(self.model)
        print(self.year)
        print(self.e.horses)
        print(self.e.type)
class engine:
    def __init__(self,h,t):
        self.horses = h
        self.type = t
    

h1 = engine ("powrer","diesel")
m1 = car ("indian","bmw",1998,h1)
m1.display()

