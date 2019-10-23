# main program
#from functions import under, over, both, grid, run
from functions import under
word = input("Please enter a word: ""\n")
print("\nEnter one of the following options:")
print(" (1) Under - display the word with a line under it.")
print(" (2) Over - display the word with a line over it")
print(" (3) Both - display the word in an underline and overline")
print(" (4) Grid - display the word in a grid that is n x n in size.")
option = input("Enter 1 to 4: ")
if option == "1":
    under(word)
    print()
elif option == "2":
    print()
elif option == "3":
    print()
elif option == "4":
    print()
else:
    print("...invalid option number")
    print()
