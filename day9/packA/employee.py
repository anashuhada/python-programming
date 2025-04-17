class Employee:

    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display_employee(self):
        print(self.id, self.name, self.salary)