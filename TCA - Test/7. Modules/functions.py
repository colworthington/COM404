# defining the functions
def under(word):
    for position in range(0, len(word), 1):
        print("" + word[position] + "")
        print("*", end="")
        #print("*" ,end="")
    #for position in range(len(word), 0, -1):
     #   print("" + position * "*" ,end="")
     #+ str(position) + ": "

def over():
    print("", word)
    for position in range(0, len(word), 1):
        print("" + str(position) + "*" ,end="")


print()