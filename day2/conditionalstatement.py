# Conditional statements
# if if...else elif

# Example 1: print a person is eligible for voting or not
# age >= 18
# age = 20
# if(age >= 18):
#     print("Eligible for voting")
# else:
#     print("Not eligible for voting")

# Example 2
# if True:
#     print("True condition")
# else:
#     print("False condition")

# Example 3
# if 0:
#     print("One")
# else:
#     print("Not one")

# Example 4: find a number is even/odd num%2 = 0
# num = 10
# if num%2 == 0:
#     print("Number is even number")
# else:
#     print("Number is odd number")

# Example 5: ternary operator - single line
# num = 13
# print("Number is even number") if num%2 == 0 else print("Number is odd number")

# Example 6: ternary operator - multiple statements in single line
a = 5
{print("Hello"), print("Python")} if a >= 10 else {print("Hi"), print("Java")}

# Example 7: Multiple conditions using elif
weekno = 10

if weekno == 1:
    print("Sunday")
elif weekno == 2:
    print("Monday")
elif weekno == 3:
    print("Tuesday")
elif weekno == 4:
    print("Wednesday")
elif weekno == 5:
    print("Thursday")
elif weekno == 6:
    print("Friday")
elif weekno == 7:
    print("Sunday")
else:
    print("Invalid weekno")