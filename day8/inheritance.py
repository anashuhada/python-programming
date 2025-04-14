# Example 1
class A:
    def m1(self):
        print("This is m1 from class A")

class B(A):
    def m2(self):
        print("This is m2 from class B")

b_obj = B()
b_obj.m1() # This is m1 from class A
b_obj.m2() # This is m2 from class B

# Example 2: single inheritance
class A:
    x, y = 10, 20

    def m1(self):
        print(self.x + self.y) # instance variables because they are tied to the object created from the class

class B(A):
    a, b= 200, 100

    def m2(self):
        print(self.a - self.b)

b_obj = B()
b_obj.m1() # 30
b_obj.m2() # 100

# Example 3: Multilevel inheritance
class A:
    x, y = 10, 20

    def m1(self):
        print(self.x + self.y) # instance variables because they are tied to the object created from the class

class B(A):
    a, b= 200, 100

    def m2(self):
        print(self.a - self.b)

class C(B):
    i, j = 5, 2

    def m3(self):
        print(self.i * self.j)

c_obj = C()
c_obj.m1() # 30
c_obj.m2() # 100
c_obj.m3() # 10

# Example 4: hierarchy inheritance
class A:
    x, y = 10, 20

    def m1(self):
        print(self.x + self.y) # instance variables because they are tied to the object created from the class

class B(A):
    a, b= 200, 100

    def m2(self):
        print(self.a - self.b)

class C(A):
    i, j = 5, 2

    def m3(self):
        print(self.i * self.j)

b_obj = B()
b_obj.m1() # 30
b_obj.m2() # 100

c_obj = C()
c_obj.m1()
c_obj.m3()

# Example: multiple inheritance > multiple parents single child
class A:
    x, y = 10, 20

    def m1(self):
        print(self.x + self.y) # instance variables because they are tied to the object created from the class

class B:
    a, b= 200, 100

    def m2(self):
        print(self.a - self.b)

class C(A, B):
    i, j = 5, 2

    def m3(self):
        print(self.i * self.j)

c_obj = C()
c_obj.m1() # 30
c_obj.m2() # 100
c_obj.m3() # 10

# Example 6: overriding; same method name, different implementation
class A:
    def m1(self):
        print("This is m1 method from class A")

class B(A): # overriding concept
    def m1(self):
        print("This is m1 method from class B")
        super().m1()

b_obj = B()
b_obj.m1()

# Example 7:
class A:
    a, b = 10, 20

class B(A):
    i, j = 100, 200
    def m(self, x, y):
        print(x + y) # local var
        print(self.i + self.j) # class var
        print(self.a + self.b) # class var

b_obj = B()
b_obj.m(1000, 2000) # 3000 300 30

# Example 8: overriding variables
class Parent:
     name = "Scott"

class Child(Parent):
    name = "John" # overriding the var value
    def test(self):
        print(super().name)

c_obj = Child()
print(c_obj.name) # John
c_obj.test() # Scott

# Example 9: overriding methods
class Bank:
    def roi(self):
        return 0

class XBank(Bank):
    def roi(self):
        return 10

class YBank(Bank):
    def roi(self):
        return 12

x_obj = XBank()
print(x_obj.roi()) # 10

y_obj = YBank()
print(y_obj.roi()) # 12

# Example 10: overloading 1 (polymorphism)
class Human:
    def sayhello(self, name=None):
        if name is not None:
            print("Hello " + name)
        else:
            print("Hello")

h = Human()
h.sayhello("John")
h.sayhello()

# Example 11: overloading 2
class Calculation:
    def add(self, a = 0, b = 0, c = 0):
        print(a + b + c)

cal = Calculation()
cal.add()
cal.add(10, 20)
cal.add(100, 200, 300)