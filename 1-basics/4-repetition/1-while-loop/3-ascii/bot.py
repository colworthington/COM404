# while loop with ascii art - allows Beep to avoid live cables
bars = int(input("How many bars should be charged? "))
charging = 0
count = 0
print("\n")
while  charging < bars:
    count = count +1
    print("Charging: " + str(count*" █"))
    charging = charging +1  
print()
print ("The battery is fully charged.")
print()