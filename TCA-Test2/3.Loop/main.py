# Code to demonstrate Loops
print()
# reading in number from user
number = int(input("How many days remain until the next full moon? "))
print("We must count the days... \n")
# while loop - count down
while number > 0:
    print("The full moon will be upon us in " + str(number) + " days.")
    number = number -1
print("\nIt's a full moon. The beast has been unleashed!\nMay it have mercy on our souls.")
print()