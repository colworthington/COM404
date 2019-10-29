# Code to demonstrate modules
height = int(input("What is your height: "))

count = 1
space_count = height
for rows in range (height):
    for spaces in range (space_count):
        print(end=' ')
    for stars in range (count):
        print ("*", end=' ')
    space_count = space_count - 1
    count = count + 1

    print()