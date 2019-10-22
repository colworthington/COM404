# Code to demonstarte loops
print()
# reading users input
zones = int(input("How many zones must I cross? "))
print("Crossing zones...")
while zones != 0:
    print("…crossed zone " + str(zones))
    zones = zones-1

print("Crossed all zones. Jumanji!")
print()