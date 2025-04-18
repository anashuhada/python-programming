# Example 1
print("This is starting point of program...")
print("This is starting point of program...")
print("This is starting point of program...")

try:
    print(x)
except:
    print("Exception occurred")

print("This is end of the program...")
print("This is end of the program...")
print("This is end of the program...")

# Example 2
print("This is end of the program...")
print("Program in progress...")
try:
    print(10/0) # 2.0
except ZeroDivisionError:
    print("Exception occurred...handled...")
print("Program completed...")

# Example 3: multiple except blocks - try, except else, finally
try:
    num1, num2 = 10, 0
    result = num1 / num2
    print("Result is: ", result)
except ZeroDivisionError:
    print("Thrown ZeroDivisionError exception...")
except SyntaxError:
    print("Thrown SyntaxError exception...")
except:
    print("Exception handled...")
else:
    print("No exceptions...")
finally:
    print("Always execute...")

# Example 4: raising our own exceptions; user defined exception error
def enter_age(num):
    if num < 0:
        raise ValueError("Only integers are allowed")
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

# enter_age(10) # Even
# enter_age(5) # Odd
# enter_age(-1) # ValueError: Only integers are allowed

print("Checking number is even or odd by calling function...")
num = -1
try:
    enter_age(num)
except ValueError:
    print("ValueError occurred and handled...")
print("Program completed...")