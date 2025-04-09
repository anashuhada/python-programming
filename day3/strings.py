# create string variable

# Example 1
s = "welcome"
s = 'welcome'
s = str("welcome")
s = str('welcome')

# create empty string variable
name = ""
name = ''
name = str()

# Example 2
# mutable: can change the value of the variable
# immutable: cannot change the value of the variable
# string is immutable

str1 = "Welcome"
print((id(str1))) # id of memory/id of variable: 4333727504

str1 = str1 + " to Python"
print((id(str1))) # previous id will be overridden: 4369941680

# if the value is changes after updating then it's immutable
# strings are immutable - creates a new string object with a different memory ID

# Example 3: + and * with str
str = "welcome"
print(str + " programming") # concatenation
print(str * 2) # print two times

# Example 4 - slicing - cut the string; [starting point will be skipped, ending index]
# starting index = 0
# ending index - 1
str = "Welcome"
print(str[1:3]) # el
print(str[:6]) # Welcom
print(str[2:]) # lcome
print(str[1:-1]) # - will remove the last char: elcom

# Example 5: ord() and chr()
print(ord('A')) # 65
print(chr(65)) # A

# Example 6: max(), min(), len()
print(max("abc")) # c
print(min("abc")) # a
print(len("welcome")) # 7

# Example 7: in, not in operators - returns true or false
s = "welcome"
print("come" in s) # True
print("lome" in s) # False
print("come" not in s) # False
print("lome" not in s) # True

# Example 8: string comparison
print("tim" == "tie") # False
print("free" != "freedom") # True
print("arrow" > "aron") # True
print("right" >= "left") # True
print("teeth" < "tee") # False
print("yellow" <= "fellow") # False
print("abc" > "") # True

# Example 9: testing strings - returns True or False
s = "welcome to python"
print(s.isalnum()) # False
print("Welcome".isalpha()) # True
print("2012".isdigit()) # True
print("first number".isidentifier()) # False
print(s.islower()) # True
print("WELCOME".isupper()) # True
print(" ".isspace()) # True

# Example 10: searching for substring
s = "welcome to python"
print(s.endswith("thon")) # True
print(s.startswith("good")) # False
print(s.find("come")) # index: 3
print(s.find("become")) # -1, not found
print(s.count("o")) # 3: returns no of occurrences of substring the string

# Example 11: converting string
s = "String in PYTHON"
s1 = s.capitalize()
print(s1) # String in python

s2 = s.title()
print(s2) # String In Python

s3 = s.lower()
print(s3) # string in python

s4 = s.upper()
print(s4) # STRING IN PYTHON

s5 = s.swapcase()
print(s5) # sTRING IN python

s6 = s.replace("in", "on")
print(s6) # Strong on PYTHON

# Example 12: reverse string
# Method 1
s = "welcome"
rev_str = ""
for i in s:
    rev_str = i + rev_str
print(s, "reversed string is: ", rev_str) # welcome reversed string is:  emoclew

# Method 2
s = "welcome"
rev_str = s[::-1] # s[start:end:remove], s[0:7:-1]
print(s, "reversed string is: ", rev_str)