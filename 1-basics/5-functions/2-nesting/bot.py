# Code to demonstrate the use of a user-defined function with a nested decision
# defining the identify listen
def identify():
    item = (input("What lies before us? "))
    if item == "a large boulder":
        print("\nIt's time to run!")
    else:
        print("\nWe will be fine")
print()


# calling the identify identify
identify()