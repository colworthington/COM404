#  code to demonstrate the use of for loops in string indexing
markings = (input("What strange markings do you see? "))
print("\nIdentifying...")
print()
for position in range(0, len(markings), 1):
    print("index " + str(position) + ": " + markings[position] + "")

print()
print("Done!")