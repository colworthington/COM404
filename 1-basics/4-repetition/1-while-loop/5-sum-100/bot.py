# Help Bop calculate the sum of the first 100 numbers
total = 0
count = 1
print("Calculating the sum of the first 100 numbers... ")
print()
while count <= 100:
    print("", total)
    total = total + count
    count = count +1

print("...Done! The answer is " + str(total) + "")
print()