# Code to demonstrate functions
def is_slow_zombie(speed):
    if speed < 5:
        return True
    else:
        return False

def take_action(mutation, speed):
    speed = is_slow_zombie(speed)
    if speed == True:
        print("This " + str(mutation) + " zombie is a slow zombie. You can run around it!\n")
    else:
        print("This " + str(mutation) + " zombie is a fast zombie. You better hide!")

def run():
    mutation = input("\nWhat is the mutation type of the zombie? ")
    speed = int(input("\nWhat is the speed of the zombie? "))
    response = input("\nWhat do you wish to do (identify or action)? ")
    if response == "identify":
        result = is_slow_zombie(speed)
        print("\nA slow zombie: " + str(result))
    elif response == "action":
        take_action(mutation, speed)
        #result = is_slow_zombie(speed)
        #print("\nA slow zombie: " + str(result))
    else:
        print("\nUnknown zombie!")

# Run the program
run()
print()