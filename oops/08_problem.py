class Employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment

    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        self.increment = ((new_salary - self.salary) / self.salary) * 100


employee = Employee(50000, 10)

print(employee.salaryAfterIncrement)

employee.salaryAfterIncrement = 60000

print(employee.increment)