# Example 1: create set
myset = {"apple", "banana", "cherry"}
print(myset) # unordered same as located in memory

# Example 2: access items from set - the only way needs to use loop
myset = {"apple", "banana", "cherry"}
for i in myset:
    print(i)

# Example 3: value exists in set or not
myset = {"apple", "banana", "cherry"}
print("banana" in myset) # True
print("banana2" in myset) # False

# Example 4: add items into set
# add() - add single item
# update() - add multiple items
myset = {"apple", "banana", "cherry"}
myset.add("orange")
print(myset) # {'orange', 'banana', 'cherry', 'apple'}

myset.update(["kiwi", "papaya"])
print(myset) # {'apple', 'kiwi', 'banana', 'cherry', 'papaya'}

# Example 5: find number of items in a set - len()
myset = {"apple", "banana", "cherry"}
print(len(myset)) # 3

# Example 6: remove item from set
# remove()
# discard()
myset = {"apple", "banana", "cherry"}
myset.remove("banana")
print(myset) # {'apple', 'cherry'}
myset.remove("xyz") # KeyError: 'xyz' - non-existing error

myset.discard("banana")
print(myset) # {'apple', 'cherry'}
myset.discard("xyz") # not throw any error

# Example 7: clear all items from set
myset = {"apple", "banana", "cherry"}
myset.clear()
print(myset) # set()

del myset
print(myset) # name 'myset' is not defined

# Example 8: join 2 sets using union()
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3) # {1, 'b', 2, 3, 'c', 'a'}

# update()
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
set1.update(set2)
print(set1) # {1, 'a', 2, 3, 'b', 'c'}

