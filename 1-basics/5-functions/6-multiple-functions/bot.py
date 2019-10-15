# code to demonstrate the implementation of multiple user defined functions
print()
# defining the function
def display_ladder(steps):
    for count in range(steps, 0, -1):
        print("| |")
        print("***")
        
def create_ladder():
    steps = int(input("How many steps remain? "))
    display_ladder(steps)

create_ladder()
print()