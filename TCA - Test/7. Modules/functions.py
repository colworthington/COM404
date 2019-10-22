# defining the functions
def under():
    print("", word)
    for position in range(0, len(word), 1):
        print(" " + str(position) + "" ,end="")

def over():
    print("", word)
    for position in range(0, len(word), 1):
        print("" + str(position) + "*" ,end="")

print()