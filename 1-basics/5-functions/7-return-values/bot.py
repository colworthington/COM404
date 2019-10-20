# code to demonstrate the use of return values
print()
# defining the function
def sum_weights(beepweight, bopweight):
    return beepweight + bopweight  
def calc_avg_weight(beepweight, bopweight):
    total = sum_weights(beepweight, bopweight)
    return total / 2
def run():
    beepweight = int(input("What is the weight of Beep? "))
    print()
    bopweight = int(input("What is the weight of Bop? "))
    print()
    response = input("What would you like to calcluate (sum or average)? ")
    if (response == "sum"):
        print()
        print("The sum of Beep and Bop's weight is:", sum_weights(beepweight, bopweight))
    elif (response == "average"):
        print()
        print("The average of Beep and Bop's weight is:", calc_avg_weight(beepweight, bopweight))
    else:
        print("I don't know that one!")
# Run the program
run()
print()
