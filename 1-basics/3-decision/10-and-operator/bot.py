#  demonstrate the use of a logical and operator
sound = (input("What did I hear? "))
print()
visual = (input("What did I see? "))
print()
if ((sound == "grrr") and (visual == "two red eyes")):
    print("There is a scary creature. I should get out of here!")
else:
    print("I am a little scared but I will continue.")
print("\n\n")
print("End.")