# Example 1: create dictionary
mydict = {
    101: "x",
    102: "y",
    103: "z"
}
print(mydict) # {101: 'x', 102: 'y', 103: 'z'}

# Example 2: access items from dictionary
mydict = {
    "brand": "Hyudai",
    "model": "i10",
    "year": 2021
}
print(mydict["brand"]) # Hyudai
print(mydict["model"]) # i10

# using get()
x = mydict.get("brand")
print(x) # Hyudai

# Example 3: change values in dictionary
mydict = {
    "brand": "Hyudai",
    "model": "i10",
    "year": 2021
}
mydict["year"] = 2020
print(mydict)

# Example 4: reading items from dictionary using loop
mydict = {
    "brand": "Hyudai",
    "model": "i10",
    "year": 2021
}
for i in mydict:
    print(i) # print only keys

for i in mydict:
    print(mydict[i]) # print only values

for i in mydict.values():
    print(i) # print only values

for k, v in mydict.items():
    print(k, ":", v) # print keys and values

# Example 5: check key is exist in dictionary or not
if "model" in mydict:
    print("Exist")
else:
    print("Not exist")

print("model" in mydict) # True

# Example 6: find number of items in dictionary
print(len(mydict)) # 3

# Example 7: add items to dictionary
mydict["color"] = "black"
print(mydict) # {'brand': 'Hyudai', 'model': 'i10', 'year': 2021, 'color': 'black'}

# Example 8: remove item from dictionary
mydict.pop("year")
print(mydict) # {'brand': 'Hyudai', 'model': 'i10'}

del mydict["year"]
print(mydict) # {'brand': 'Hyudai', 'model': 'i10'}

del mydict
print(mydict) # name 'mydict' is not defined

mydict.clear()
print(mydict) # {}

# Example 9: copy dictionary
mydict1 = {
    "brand": "Hyudai",
    "model": "i10",
    "year": 2021
}
mydict2 = mydict1
print(mydict2)

mydict2 = mydict1.copy()
print(mydict2)