# code to demonstrate nesting
health = 100
count = 5
print()
print("Your health is 100%. Escape is in progress...")
print()
for count in range(count, 0, -1):
    print()
    response = input("…Oh dear, who is that? ")
    if response == "Smiler's Bot":
        health = health-20
        print("Time to jam out of here!")
    elif response == "Hacker":
        health = health+20
        print("Yay! Better follow this one!")
    else:
        print("Phew, just another emoji!")
print()
print("Escaped! Health is " + str(health) + "%")
