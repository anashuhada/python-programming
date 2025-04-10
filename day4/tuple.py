# Example 1: create tuple
mytuple = ("apple", "banana", "cherry")
print(mytuple) # ('apple', 'banana', 'cherry')
mytuple = () # empty tuple

# Example 2: access tuple items - use index
mytuple = ("apple", "banana", "cherry")
print(mytuple[1]) # banana
print(mytuple[-1]) # cherry

# Example 3: range of indexes
mytuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(mytuple[2:5]) # ('cherry', 'orange', 'kiwi')
print(mytuple[-4:-1]) # ('orange', 'kiwi', 'melon')

# Example 4: change tuple items
# By default tuple doesn't allow you change values because it's immutable
# Work around: tuple > list(modify) > tuple
mytuple = ("apple", "banana", "cherry")
mylist = list(mytuple)
# print(mylist) # ['apple', 'banana', 'cherry']
mylist[0] = "orange" # change the value
mytuple = tuple(mylist) # convert to tuple back; ('orange', 'banana', 'cherry')
print(mytuple)

# Example 5: reading tuple items using loop
mytuple = ("apple", "banana", "cherry")
for i in mytuple:
    print(i)

# Example 6: check if item exists - searching for item in tuple
mytuple = ("apple", "banana", "cherry")
if "banana" in mytuple:
    print("Yes, banana is present")
else:
    print("No, banana is not present")

# Example 7: tuple length - counting items in a tuple
mytuple = ("apple", "banana", "cherry")
print(len(mytuple)) # 3

# Example 8: add items to tuple
mytuple = ("apple", "banana", "cherry")
mytuple[0] = "orange"
print(mytuple) # # TypeError: 'tuple' object does not support item assignment

# Example 9: copy tuple
mytuple1 = ("apple", "banana", "cherry")
mytuple2 = mytuple1
print(mytuple2)

# Example 10: remove items from tuple - not possible because tuple is immutable
mytuple = ("apple", "banana", "cherry")
# mytuple.remove("apple") # invalid/impossible

del mytuple
print(mytuple) # name 'mytuple' is not defined

# Example 11: join/combine tuple
tuple1 = (10, 20, 30)
tuple2 = ('a', 'b', 'c')
tuple3 = tuple1 + tuple2
print(tuple3)

# Example 12: tuple comparison
tuple1 = (10, 20, 30)
tuple2 = ('a', 'b', 'c')
if tuple1 == tuple2:
    print("Tuples are equal")
else:
    print("Tuples are unequal")