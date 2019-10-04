# Beep is looking for his spare battery.
# ask question
look = (input("Where should I look? "))
if (look == "in the bedroom"):
    print()
    # look where?
    where1 = (input("Where in the bedroom should I look? "))
    if (where1 == "under the bed"):
        print()
        print("Found some shoes but no battery")
    else:
        print()
        print("Found some mess but no battery.")
elif (look == "in the bathroom"):
    print()
    # look where?
    where2 = (input("Where in the bathroom should I look? "))
    if (where2 == "in the bathtub"):
        print()
        print("Found a rubber duck but no battery")
    else:
        print()
        print("It is wet but I found no battery.")
elif (look == "in the lab"):
    print()
    # look where?
    where3 = (input("Where in the lab should I look? "))
    if (where3 == "on the table"):
        print()
        print("Yes! I found my battery!")
    else:
        print()
        print("Found some tools but no battery.")
# anything else entered
else:
    print()
    print("I do not know where that is but I will keep looking.")
    print()
print()