# break and continue
for i in range(1, 10):
    if i == 5:
        print("Break at 5")
        break
    print(i)
print("Program exited!")

for i in range(1, 10):
    if i == 3 or i == 5 or i ==7:
        continue # skipped at 5
    print(i)
print("Program exited!")

for i in range(3, 7, 2):
    print(i)