# code to demonstrate decisions if…elif...else statement
print()
print("Learn the steps of the 5 sequence tango.")
# variable steps
steps = input("What step do you wish to learn? ")
# print statement depending on response 1-5
if steps == "1":
    print("Leader takes a step back.")
elif steps == "2":
    print("Side step towards centre of floor.")
elif steps == "3":
    print("Leader steps outside of follower.")
elif steps == "4":
    print("Preparation of the cross with the forward step.")
elif steps == "5":
    print("Leader closes his feet, follower completes cross step.")
# if 1-5 is not chosen
else:
    print("\nTerminate the sequence.")

print()
