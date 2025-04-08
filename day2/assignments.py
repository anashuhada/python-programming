# Assignment 1
num = -10

if num > 0:
    print("Positive number")
else:
    print("Negative number")

print("Positive number") if num > 0 else print("Negative number")

# Assignment 2
a = 30
b = 20

if a > b:
    print("The largest number: ", a)
else:
    print("The largest number: ", b)

print("The largest number: ", a) if a > b else print("The largest number: ", b)

# Assignment 3
a = 30
b = 20
c = 50

if a >= b and a >= c:
    num = a
    print("The largest number:", num)
if b >= a and b >= c:
    num = b
    print("The largest number:", num)
else:
    num = c
    print("The largest number:", num)

# Assignment 4
weekname = input("Enter week name: ").strip().capitalize()

if weekname == "Sunday":
    print(1)
elif weekname == "Monday":
    print(2)
elif weekname == "Tuesday":
    print(3)
elif weekname == "Wednesday":
    print(4)
elif weekname == "Thursday":
    print(5)
elif weekname == "Friday":
    print(6)
elif weekname == "Saturday":
    print(7)
else:
    print("Invalid week name")
