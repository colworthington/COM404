# code to demonstrate the use of one loop nested in another
rows = int(input("How many rows should I have? "))
print()
columns = int(input("How many columns should I have? "))
print()
print("Here I go...")
print()
for count in range(rows):
    for number in range(columns):
        print(":-) ", end="")
    print()

print("\nDone!")