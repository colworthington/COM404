# code to demonstrate nesting
print("\nWelcome to the Planet of the Apes...")
human_count = 0
ape_count = 0
for count in range(7, 0, -1):
    response = input("...be ye human or be ye ape? ")
    if response == "Human":
        print("I did not start this war. But I will finish it.\n")
        human_count = human_count +1
    elif response == "Ape":
        print("Apes together strong!\n")
        ape_count = ape_count +1
    else:
        print("This is not your fight.")

print("\nTotal humans encountered: " +str(human_count))
print("Total apes encountered: " +str(ape_count))
print()
