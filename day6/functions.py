# Example 1
def myfunc():
    print("Hello")

myfunc() # call the function

# Example 2
def myfunc(name):
    print("Hello,", name)
myfunc("John") # Hello, John

# Example 3
def calculate(a, b):
    return (a+b)
# sum = calculate(20, 50)
# print(sum)
print(calculate(20, 50))

# Example 4
def func():
    # return
    i = 10 # None
print(func()) # None

# Example 5
def cal(a, b):
    # print(a + b)
# cal(10, 50)  # 60
    return (a + b)
print(cal(10, 50)) # 60