# defining the functions
def under(word):
    print("\n" + word)
    # print(len(word))
    #for position in range(0, len(word), 1):
    #    print(word[position], end="")
    for position in range(0, len(word), 1):
        print("*", end="")
    print()

def over(word):
    print()
    for position in range(0, len(word), 1):
        print("*", end="")
    print("\n" + word)

def both(word):
    print()
    for position in range(0, len(word), 1):
        print("*", end="")
        print("\n" + word, end="")
    for position in range(0, len(word), 1):
        print("*", end="")

def grid(word, size):
    print()
    char = len(word)
    count2 = size
    while count2 != 0:
        for count in range(size, 0, -1):
            print(char * "*", "  ", end="")
        print()
        for count in range(size, 0, -1):
            print("" + str(word) + " | ", end="")
        print()
        for count in range(size, 0, -1):
            print(char * "*", "  ", end="")
        print()
        count2 = count2-1
    # both(word)
