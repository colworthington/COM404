# Code to demonstrate functions and function calls
def isFusionShot(slug1, slug2):
    if slug1 == "Infurnus" and slug2 == "Infurnus":
        print("True")
        return True
    elif slug1 == "AquaBeek" and slug2 == "AquaBeek":
        print("True")
        return True
    else:
        print("False")
        return False

def isDefectiveShot(slug1, slug2):
    print()
    answer = isFusionShot(slug1, slug2)
    if answer != True:
        return True
        print("True")
    elif answer == False:
        print("False")
        return False
    
def run():
    print()
    slug1 = input("Enter the type for the first slug (Infurnus or AquaBeek): ")
    slug2 = input("Enter the type for the second slug (Infurnus or AquaBeek): ")
    response = input("\nPlease enter the word fusion or defective: ")
    if response == "fusion":
        isFusionShot(slug1, slug2)
    elif response == "defective":
        isDefectiveShot(slug1, slug2)
    elif response != "fusion" or "defective":
        print("\nInvalid selection. Please try again")
   
# Run the program
run()
print()