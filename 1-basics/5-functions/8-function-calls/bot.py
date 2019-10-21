# code to demonstrate the use of multiple function calls
print()
word = "Hello"
def ascii_box(number):
    for count in range(number, 0, -1):
        print("##########")
        print("# " + str(word) + " #")
        print("##########")
def lower_case(number):
    print("")
def upper_case(number):
    print("")
def mirrored(number):
    print("")
def run():
    number = int(input("How many times to display word? "))
    print()
    ascii_box(number)
run()