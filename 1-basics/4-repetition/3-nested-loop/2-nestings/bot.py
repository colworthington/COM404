# code to demonstrate the use of nested loops and decisions
sequence = (input("Please enter a sequence? "))
print()
character = (input("Please enter the character for the marker? "))
print()
for count in range(0, sequence, 1):
    for number in range(0, character, 1):
        print("The distance between the markers is ", end="")
    print()

print("\nEnd.")
