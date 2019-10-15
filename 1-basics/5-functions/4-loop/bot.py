# code to demonstrate the use of a user-defined function with a loop
print()
# defining the function
def cross_bridge(steps):
    if steps > 5:
        print("The bridge is collapsing!")
        for count in range(steps, 0, -1):
            print("Crossed steps")
    if steps <= 5:
        for count in range(steps, 0, -1):
            print("Crossed steps")
    else:
        print("we must keep going!")

# calling escape_by function
cross_bridge(3)
cross_bridge(6)

print() 