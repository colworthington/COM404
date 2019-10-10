# code to demonstrate step value of the range function
# enter even number
level = int(input("What level of brightness (even number) is required? "))
print("\nAdjusting brightness..")
print()
for count in range(2, level+2, 2):
    print("Beep's brightness level:" + count * " *")
    print("Bop's brightness level:" + count * " *")
    print()
print()
print("Adjustments complete!")