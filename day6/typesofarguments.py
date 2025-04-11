# # Example 1
def func(i, j):
    print(i, j)
# func(100, 200) # positional arguments, must follow the param
func(j=200,i=100) # keyword arguments, assign based on the param, not following the seq

# Example 2
def func(i, j=10):
    print(i,j)
# func(10,200) # 10 200
func(500) # 500 10

# Example 3: keyword arguments
def greetings(name, greetmsg):
    print(greetmsg + " " + name)
greetings(name="John", greetmsg="Hi") # Hi John
greetings(greetmsg="Hi", name="John") # Hi John

# Example 4
def myfunc(a, b, c):
    print(a, b, c)
myfunc(10, 20, 30) # 10 20 30; positional argument
myfunc(a=10, b=20, c=30) # 10 20 30; keyword argument
myfunc(b=50, c=70, a=100) # 100 50 70; keyword argument
myfunc(50, 70, c=100)
# myfunc(50, b=70, 100) # positional argument must appear before keyword argument
myfunc(50, 70, b=100) # logical error

# Example 5: function returns multiple values
def largest(a, b):
    if a > b:
        return a, b
    else:
        return b, a
print(largest(100, 200)) # (200, 100)
print(largest(20, 10)) # (20, 10)

res = largest(10, 20)
print(type(res)) # tuple