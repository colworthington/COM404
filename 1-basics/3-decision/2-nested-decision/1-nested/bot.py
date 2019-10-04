# Allows Beep to classify his books
# ask question
cover = (input("What type of cover does the book have? (hard or soft) "))
# if soft cover chosen
if (cover == "soft"):
    print()
    # perfect bound yes/no
    answer = (input("Is the book perfect-bound? (yes/no) "))
    if (answer == "yes"):
        print()
        print("Soft cover, perfect bound books are very popular!")
        print()
    else:
        print()
        print("Soft covers with coils or stitches are great for short books.")
        print()
# hard cover
else:
    print()
    print("Books with hard covers can be more expensive!")
    print()