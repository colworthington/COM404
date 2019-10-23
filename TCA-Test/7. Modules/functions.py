# defining the functions
def under(word):
    print("\n" + word)
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
    print("\n" + word)
    for position in range(0, len(word), 1):
        print("*", end="")

print()