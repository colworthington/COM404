# Code to demonstrate nesting
dead_ends = 0
mummies = 0
print("\nEscaping the tomb...")
for count in range(4, 0, -1):
    print()
    response = input("What lies before me? ")
    if response == "a dead end":
        print("Time to turn back.")
        dead_ends = dead_ends +1
    elif response == "a mummy":
        print("Better find another way.")
        mummies = mummies +1
    else:
        print("Let's move around it.")
print("\nEncountered " +str(dead_ends) + " dead ends and " + str(mummies) + " mummies.\n")