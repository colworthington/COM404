# Ask user for phrase
phrase = (input("What phrase do you see? "))

# Identify markings
print("\nReversing...\nThe phrase is ", end="")

reversed = ""

for letter in phrase:
    reversed = letter + reversed

print(reversed)
print()