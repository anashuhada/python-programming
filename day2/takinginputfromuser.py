# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")

# print(type(num1))
# print(type(num2))

# print(num1 + num2) # 1020, str not int

# Approach 1
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# print(type(num1)) # int
# print(type(num2)) # int
#
# print(num1 + num2) # 30

# Approach 2
# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")
#
# print(type(num1)) # str
# print(type(num2)) # str
#
# print(int(num1) + int(num2)) # 30

# Approach 3
num1 = input("Enter first decimal number: ")
num2 = input("Enter second decimal number: ")

print(type(num1)) # str
print(type(num2)) # str

print(float(num1) + float(num2)) # 130.4