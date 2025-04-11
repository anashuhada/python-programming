# Example 1
global_var = 20 # global variable

def func():
    local_var = 10 # local variable; accessible in the function
    print(local_var) # 10
    print(global_var) # 20
func()
# print(local_var) # invalid because it's local var of function
print(global_var) # valid because it's global var

# Example 2
xy = 100 # global var

def cool():
    xy = 200 # local var
    print(xy)
cool() # 200

# Example 3
xy = 100 # global var

def cool():
    global xy
    xy = 300 # refer to global var but with a modification
    print(xy)
cool() # 300
print(xy) # 300

# Example 4
x = 100

def cool():
    global x
    x = 500
    print(x)
# cool() # 500
print(x) # 100; if not invoking the function, the value won't be updated

# Example 5
# there's no need to declare global variables outside the function
# can declare the global inside the function using global keyword
def cool():
    global x
    x = 500
    print(x)
cool() # 500
print(x) # 500; accessible x because it's global variable
