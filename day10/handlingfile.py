# Example 1: writing data into text file
file = open("/Volumes/KINGSTON/Software Testing/Python Programming/File/myfile.txt", "w") # writing mode
file.write("This is my first statement\n")
file.write("This is my second statement\n")
file.write("This is my third statement\n")
file.write("This is my fourth statement\n")
file.write("This is my fifth statement\n")
file.close() # it will use some memory and might not able to delete or having other issues
print("Program completed...")

# Example 2: reading data from text file
file = open("/Volumes/KINGSTON/Software Testing/Python Programming/File/myfile.txt", "r") # read data
# print(file.read())
print(file.readline()) # This is my first statement
file.close()

# Example 3: appending data into text file
file = open("/Volumes/KINGSTON/Software Testing/Python Programming/File/myfile.txt", "a")
file.write("This is my sixth line \n")
file.write("This is my seventh line \n")
file.close()
print("Program completed")