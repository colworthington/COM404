# code to demonstrate step value of the range function
# range(1, 6, 1) produces the following list of numbers: 1, 2, 3, 4, 5, natural numbers
# range(1, 6, 2) produces the following list of numbers: 1, 3, 5, odd numbers
# range(0, 6, 2) produces the following list of numbers: 0, 2, 4 even numbers
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