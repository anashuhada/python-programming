class Student:

    def __init__(self, id, name, grad):
        self.id = id
        self.name = name
        self.grad = grad

    def display_student(self):
        print(self.id, self.name, self.grad)