# code to demonstrate the use of a user-defined function with multiple parameters
print()
# defining the function
def climb_ladder(remaining, crossed):
    if int(crossed) > int(remaining):
        print("Still some way to go!")
        return climb_ladder
    else:
        print("We made it!")

# calling the function
climb_ladder(5, 5)
climb_ladder(6, 5)