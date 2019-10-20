# code to demonstrate the use of return values
print()
# defining the function
def sum_weights(beepWeight, bopWeight):
    sum_weights = int(beepweight) + int(bopweight) 
    return sum_weights    
def calc_avg_weight(beepWeight, bopWeight):
    calc_avg_weight = sum_weights()
    return calc_avg_weight
def run():
    beepweight = int(input("What is the weight of Beep? "))
    bopweight = int(input("What is the weight of Bop? "))
    response = input("What would you like to calcluate (sum or average)? ")
    if (response == "sum"):
        sum_weights()
        # print("total weight = " sum_weights()"")
    elif (response == "average"):
        print()
        calc_avg_weight()
        # print("average weight = " calc_avg_weight()"")
    else:
        print("I don't know that one!")
# Run the program
run()
