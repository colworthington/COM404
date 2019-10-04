# Operators
print("Please enter a whole number...")
number = int(input())
# Carry out a calculation for the check
check = int(number/2)*2
# If the result does not equal 0 then it is an odd number
if (number != check):
    print()
    print("The number " + str(number) + " is an odd number.")
    print()
# Otherwise it is an even number
else:
    print()
    print("The number " + str(number) + " is an even number.")
    print()

print()
print("Complete")
print()