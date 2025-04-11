# Example 1
class MyClass:
    def myfun(self): # self belongs to the particular class
        pass
    def display(self, name):
        print(name)

mc1 = MyClass() # object
mc2 = MyClass()

mc1.myfun()
# mc1.display() # John
mc1.display("David") # David

# Example 2
class MyClass:
    def m1(self):
        print("This is intance method") # invoke through object only

    @staticmethod # common method for every object
    def m2(self, num):
        print(self, num) # directly invoke using class

mc = MyClass()
mc.m1()
MyClass.m2(100, 200)

# Example 3
class MyClass:
    a, b = 10, 20 # class variables

    def add(self):
        print(self.a + self.b)

    def mul(self):
        print(self.a * self.b)

mc = MyClass()
mc.add() # 30
mc.mul() # 200

# Example 4
i, j = 15, 25 # global variables

class MyClass:
    a, b = 10, 20 # class variables

    def add(self, x, y): # x, y are local variables
        print(x + y) # x, y are local variables
        print(self.a + self.b) # a, b are class variables
        print(i + j) # i, j are global variables

mc = MyClass()
mc.add(100, 20)

# Example 5: same variable names
a, b = 15, 25 # global variables

class MyClass:
    a, b = 10, 20 # class variables

    def add(self, a, b):
        print(a + b) # local
        print(self.a + self.b) # class
        print(globals()['a'] + globals()['b']) # global

mc = MyClass()
mc.add(100, 20)

# Example 6: one class can have multiple objects
class MyClass:
    def display(self, name):
        print("This is display method")
        print(name)

obj1 = MyClass()
obj1.display("David")

obj2 = MyClass()
obj2.display("Jasmine")

# Example 7
class MyClass:
    def __init__(self): # constructor; no need to create object - automatically executed once creation of object
        print("This is constructor")
    def m1(self): # call this method through object
        print("Hello")
    def m2(self, x, y):
        return x + y

mc = MyClass() # invoke constructor automatically
mc.m1() # method we have to call explicitly by using object
res = mc.m2(10, 20)
print(res)

# Example 8
class MyClass:
    name = "John"

    def __init__(self, name): # constructor expecting one argument
        print(name) # local var
        print(self.name) # class var

mc = MyClass("David") # pass parameter to the constructor

# Example 9
# Req: Employee class
# Constructor: emp_id, emp_name, salary
# display(): print all the values
class Employee:
    def __init__(self, emp_id, emp_name, salary):
        self.emp_id = emp_id # convert local var to class var
        self.emp_name = emp_name
        self.salary = salary
    def display(self):
        print(self.emp_id, self.emp_name, self.salary)

emp1 = Employee(101, "John", 5000)
emp1.display()

emp2 = Employee(102, "Alicia", 7000)
emp2.display()

# Example 10
# Req: Employee class
# Constructor: emp_id, emp_name, salary
# Constructor: print all the values
class Employee:
    def __init__(self, emp_id, emp_name, salary):
        self.emp_id = emp_id # convert local var to class var
        self.emp_name = emp_name
        self.salary = salary
    def __str__(self): # return only string data type
        return self.emp_name

emp1 = Employee(101, "John", 5000)
print(emp1)
