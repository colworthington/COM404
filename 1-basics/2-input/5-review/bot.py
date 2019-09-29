# A basic input/output program
print("What is your ideal Body Mass Index? (bmi)")
bmi = float(input())
print()
print("How tall are you? (in meters)")
# height to take in decimal input
height = float(input())
print()
# Ideal Weight calculated by 
weight = bmi*(height*height)
print("So for a BMI of... "+ str(bmi) +" a height that = " + str(height) + "m, your ideal weight is " + format(weight, '.2f') + "kg.")