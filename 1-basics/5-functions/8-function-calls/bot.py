# code to demonstrate the use of multiple function calls
print()
def ascii_box(word):
    print()
    for position in range(0, len(word)+4, 1):
        print("#", end="")
    print("\n# " + str(word) + " #")
    for position in range(0, len(word)+4, 1):
        print("#", end="")
    print()

def lower_case(word):
    print()
    new_word = word.lower()
    print ("lower case: "+ new_word)

def upper_case(word):
    print()
    new_word = word.upper()
    print ("UPPER case: "+ new_word)
    
def mirrored(word):
    print()
    reversed = ""
    for letter in word:
        reversed = letter + reversed
    print("Mirrored: " + word + " |", reversed)
    
def repeat(number, word):
    while number > 0:
        print()
        new_word = word.lower()
        print ("lower case: "+ new_word)
        number = number -1
        new_word = word.upper()
        print ("UPPER case: "+ new_word)
        

def run():
    word = input("Enter a word: ")
    print("\nEnter one of the following options:")
    print(" (1) Display the word in a box.")
    print(" (2) Display the word in lower case.")
    print(" (3) Display a word in UPPER case")
    print(" (4) Display word mirrored.")
    print(" (5) Repeat the word.")
    option = input("Enter 1 to 5: ")
    if option == "1":
        ascii_box(word)
        print()
    elif option == "2":
        lower_case(word)
        print()
    elif option == "3":
        upper_case(word)
        print()
    elif option == "4":
        mirrored(word)
        print()
    elif option == "5":
        number = int(input("How many times to display word? "))
        repeat(number, word)
    else:
        print("\nI do not know that option.")
    
run()