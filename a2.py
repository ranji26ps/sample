class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
    def annual_salary(self):
        return self.salary * 12
   
emp1 = Employee("Ranjith", 5000, "Engineering")
print(f"{emp1.name}'s annual salary: {emp1.annual_salary()}")