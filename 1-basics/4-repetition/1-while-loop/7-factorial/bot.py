# a while loop in calculating the factorial of a number
number = int(input("Please enter a number: "))
count = number-1
answer = number
while count > 0 :
    answer = answer * count
    count = count -1
    
print("\n The factorial is " +str(answer) + "")