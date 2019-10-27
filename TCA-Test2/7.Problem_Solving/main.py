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
    

message = input("Enter a message: ")
print("\nEnter one of the following options:")
print(" (1) Under - display the message with a line under it.")
print(" (2) Over - display the message with a line over it")
print(" (3) Both - display the message in an underline and overline")
print(" (4) Grid - display the message in a grid that is n x n in size.")
option = input("Enter 1 to 4: ")
if option == "1":
    under(message)
    print()
elif option == "2":
    over(message)
    print()

