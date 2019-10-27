# Code to demonstrate functions
# creating a function
print()
def cast_spell_with(ingredient):
    print("Double, double toil and trouble. Fire burn and caldron bubble.")
    if ingredient == "newt":
        print("In goes the eye of a newt that is not so cute.\n")
    elif ingredient == "toad":
        print("In goes a toad to add to our horrible load.\n")
    else:
        print("In goes an ingredient unknown for a spell that will be overblown.\n")
    print
# running function
cast_spell_with("newt")
cast_spell_with("toad")
cast_spell_with("bat")