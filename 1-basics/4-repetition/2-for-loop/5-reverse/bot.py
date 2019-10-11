#  code to demonstrate how to reverse a string using a for loop
phrase = (input("What phrase do you see? "))
print("\nReversing...")
print()
print("The phrase is: ",end="")
for position in range(len(phrase), 0, -1):
        print(""+ phrase[position-1] + "",end="")

print("\n")
print("Done!")