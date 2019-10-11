# code to demonstrate the use of one loop nested in another
rows = (input("How many rows should I have? "))
print()
columns = (input("How many columns should I have? "))
print()
print("Here I go...")
for count in range(0, rows, 1):
    for number in range(0, columns, 1):
        print(number, "", end="")
    print()

print()
print("End.")