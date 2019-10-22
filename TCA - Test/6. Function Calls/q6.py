# code with three functions
print()
def is_league_united(hero1,hero2):
    if hero1 == "Superman" and hero2 == "Wonder Woman":
        print("True")
        return True
    else:
        print("False")
        return False

def decide_plan(hero1,hero2):
    answer = is_league_united(hero1,hero2)
    if answer == True:
        print("Time to save the world!")
    else:
        print("We must unite the league!")

def run():
    hero1 = input("Enter name of the first hero: ")
    hero2 = input("Enter name of the second hero: ")
    response = input("Enter league or plan: ")
    if response == "league":
        is_league_united(hero1,hero2)
    elif response =="plan":
        decide_plan(hero1,hero2)
    else:
        print("I don't know that one!")

# Run the program
run()
print()
