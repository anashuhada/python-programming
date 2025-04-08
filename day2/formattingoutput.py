# name = "john"
# age = 30
# salary = 5000.50

name, age, salary = "john", 30, 5000.50

# Approach 1
# print(name)
# print(age)
# print(salary)
# print(name, age, salary)

# Approach 2
# print("Name is: ", name)
# print("Age is: ", age)
# print("Salary is: ", salary)

# Approach 3
print("Name is: %s Age is: %d Salary is: %g" %(name, age, salary))

# Approach 4
print("Name is: {} Age is: {} Salary is: {}" .format(name, age, salary))

# Approach 5
print(f"Name is: {name} Age is: {age} Salary is: {salary}")
