# Retrieve Parcel details from user
print("What size is the parcel? ")
size = input()
print("What is weight of the parcel? ")
weight = input()
print("Do you want fast delivery? ")
delivery = input()   
# Identify and display the category
if ((size == "big") and (weight == "heavy") and (delivery == "yes")):
    print()
    print("This parcel will be very expensive to deliver.")
elif ((size == "medium") or (weight == "average") and (delivery != "yes")):
    print()
    print("This parcel will be a standard price to deliver.")
else:
    print()
    print("This parcel will be inexpensive to deliver.")
print("\n\n")
print("End.")