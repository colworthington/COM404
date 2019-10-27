# Code to demonstrate problem solving
def under(message):
    print("\nHalloween")
    count = len(message)
    print(count * "-", end="")
    print("\n" + str(message))

def over(message):
    count = len(message)
    print("\n" + str(message))
    print(count * "-", end="")
    print("\nHalloween")

def both(message):  
    count = len(message)
    print("\n" + str(message))
    print(count * "-", end="")
    print("\nHalloween")
    print(count * "-", end="")
    print("\n" + str(message))
    

def grid(value):
    if value > 5:
        value = 5
    count2 = value
    print()
    while count2 != 0:
        for count in range(value):
            print("Halloween", end="")
            print("|", end="")
        count2 = count2 -1
        print()
    print()

print("\nEnter one of the following options:")
print(" (1) Under - display the message with a line under it.")
print(" (2) Over - display the message with a line over it")
print(" (3) Both - display the message in an underline and overline")
print(" (4) Grid - display Halloween in a grid that is n x n in size.")
option = input("Enter 1 to 4: ")
if option == "1":
    message = input("Enter a message: ")
    under(message)
    print()
elif option == "2":
    message = input("Enter a message: ")
    over(message)
    print()
elif option == "3":
    message = input("Enter a message: ")
    both(message)
    print()
elif option == "4":
    value = int(input("Please enter value for grid: "))
    grid(value)
else:
    print("\nI do not know that option.")


