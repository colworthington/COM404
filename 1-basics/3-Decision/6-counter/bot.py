# mathematical operators -  enter 3 numbers (one number at a time) and should work out how many of these are even and odd
print("Please enter the first whole number...")
num1 = int(input())
print()
print("Please enter the second whole number...")
num2 = int(input())
print()
print("Please enter the third whole number...")
num3 = int(input())
print()
evencount = 0
oddcount = 0
if (num1 %2 > 0):
    oddcount = oddcount + 1
else:
    evencount = evencount + 1
if (num2 %2 > 0):
    oddcount = oddcount + 1
else:
    evencount = evencount + 1
if (num3 %2 > 0):
    oddcount = oddcount + 1
else:
    evencount = evencount + 1

print()
print("There were " + str(evencount) + " even and " + str(oddcount) + " odd numbers.")
print()
print("Completed.")