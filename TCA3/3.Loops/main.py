# code to demonstrate loops
print()
# set variables and read input
number = int(input("How many heroes must we gather? "))
count = 1
print("Gathering heroes...")
while number > 0:
    print("...found hero " + str(count))
    count = count+1
    number = number-1
print("...all the heroes have been gathered\n")

