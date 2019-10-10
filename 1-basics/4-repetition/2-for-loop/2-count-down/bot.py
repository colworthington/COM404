# code to demonstrate counting down with a for loop
number = int(input("How far are we from the cave? "))
print("\nResult..")
for count in range(number, 0, -1):
    print("" + str(count) + " steps remaining")

print()
print("We have reached the cave!")