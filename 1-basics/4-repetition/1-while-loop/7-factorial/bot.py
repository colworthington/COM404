# a while loop in calculating the factorial of a number
number = int(input("Please enter a number: "))
# sets count at number -1
count = number -1
total = number
while count > 0 :
    total = total * count
    count = count -1    
    
print("\n The factorial is " +str(total) + "")