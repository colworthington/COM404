# Ask user for phrase
phrase = (input("What phrase do you see? "))

# Identify markings
print("\nReversing...")

reversed = " "
for letter in phrase:
    reversed = letter + reversed

print("The phrase is", reversed, end="")
#print(reversed)
print()