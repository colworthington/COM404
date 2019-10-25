# while loop with ascii art - allows Beep to avoid live cables
bars = int(input("How many bars should be charged? "))
charging = 0
#count = 0
print()
while  charging < bars:
    #count = count +1
    charging = charging +1
    # print("Charging: " + str(count*" █"))
    print("Charging: " + str(charging*" █"))
print()
print ("The battery is fully charged.")
print()