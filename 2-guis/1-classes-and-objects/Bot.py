# Code to demonstrate the implementation of a class and object
class Bot:
    def __init__(self, name, age, energy, shield_level):
        #self.name = "Bop"
        #self.age = "30"
        #self.energy = "5"
        #self.shield_level = "8"
        #self.summary = ""
        self.name = name
        self.age = age
        self.energy = energy
        self.shield_level = shield_level
        #self.summary = ""

    def display_name(self):
        print()
        print(" #########")
        print(" #  {}  #".format(self.name))
        print(" #########") 
        
    def display_age(self):
        print()
        print("     {}  ".format(self.age))
        print("     ##")
        print("    ####")
        print(" ##########")
        print(" #  ####  #")
        print(" ##########")
        print()

    def display_energy(self):
        total = int(self.energy)
        print("Energy: " + total*"♦")
        print()

    def display_shield(self):
        total2 = int(self.shield_level)
        print("Shield: " + total2*"█")
        print()

    def __str__(self):
        return("{} is {} years old, energy:{} , shield:{} \n".format(self.name, self.age, self.energy, self.shield_level))
        

bop = Bot("Bop", 30, 5, 8)
#bop.display_name()
#bop.display_age()
#bop.display_energy()
#bop.display_shield()
print(bop.__str__())