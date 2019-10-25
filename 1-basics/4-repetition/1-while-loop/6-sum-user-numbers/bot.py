# provide some random numbers so that it can calculate the sum of the specified numbers
numbers = int(input("How many numbers should I sum up? "))
print()
count = 1
total = 0
while count <= numbers:
    num = int(input("Please enter number " + str(count) + " of " + str(numbers) + " "))
    count = count + 1
    total = total + num
print("\nThe answer is " +str(total) + "")