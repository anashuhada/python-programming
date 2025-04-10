# Example 1: how to create list

mylist1 = [10, 20, 30, 40, 50] # number of list
mylist2 = ["apple", "banana", "cherry"] # string of list
mylist3 = ["apple", 10, "banana", 20]
mylist = list() # empty list

print(mylist1)
print(mylist2)
print(mylist3)
print(mylist)

# Example 2: accessing items from the list
mylist = ["apple", "banana", "cherry"] # index starts with 0
print(mylist[0])
print(mylist[1])
print(mylist[-1]) # last index
print(mylist[-2])

# Example 3: range of indexes
mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist[2:5]) # ['cherry', 'orange', 'kiwi']
print(mylist[-4:-1]) # count from the end; last index not displayed, ['orange', 'kiwi', 'melon']

# Example 4: change item value
mylist = ["apple", "banana", "cherry"]
print(mylist) # ['apple', 'banana', 'cherry']

mylist[1] = "orange"
print(mylist) # ['apple', 'orange', 'cherry']

# Example 5: read items in the list using loop
mylist = ["apple", "banana", "cherry"]
for i in mylist:
    print(i)

# Example 6: check if the item is existed in the list or not
mylist = ["apple", "banana", "cherry"]
if "apple" in mylist:
    print("Yes, apple is present")
else:
    print("No, apple is not present")

# Example 7: list length (count number of items in a list)
mylist = ["apple", "banana", "cherry"]
print (len(mylist)) # 3

# Example 8: add items; append() and insert()
mylist = ["apple", "banana", "cherry"]
mylist.append("orange") # add new value at the end of the list
print(mylist) # ['apple', 'banana', 'cherry', 'orange']

mylist.insert(1, "kiwi") # include the required index, value; the current list will be shifting to the next
print(mylist) # ['apple', 'kiwi', 'banana', 'cherry', 'orange']

# Example 9: remove item from the list
mylist = ["apple", "banana", "cherry"]
print(mylist.pop(0)) # specify the index not the value
print(mylist) # ['banana', 'cherry']

# del keyword
mylist = ["apple", "banana", "cherry"]
del mylist[2] # remove single item based on the index
print(mylist) # ['apple', 'banana']

# clear()
mylist = ["apple", "banana", "cherry"]
mylist.clear()
print(mylist) # []

# Example 10: copy list; list()
mylist1 = ["apple", "banana", "cherry"]
mylist2 = list(mylist1)
print(mylist1) # ['apple', 'banana', 'cherry']
print(mylist2) # ['apple', 'banana', 'cherry']

# copy()
mylist1 = ["apple", "banana", "cherry"]
mylist2 = mylist1.copy()
print(mylist1) # ['apple', 'banana', 'cherry']
print(mylist2) # ['apple', 'banana', 'cherry']

# Example 11: combine/join lists using + operator
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# using loop statement
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
for i in list2:
    list1.append(i)
print(list1) # ['a', 'b', 'c', 1, 2, 3]

# using extend
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

# Example 12: list comparison
mylist1 = [10, 20, 30]
mylist2 = ['a', 'b', 'c']
if mylist1 == mylist2:
    print("Lists are equal")
else:
    print("Lists are unequal")