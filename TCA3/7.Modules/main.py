# Code to demonstrate modules
#height = int(input("What is your number: "))

#count = 1
#space_count = height
#for rows in range (height):
 #   for spaces in range (space_count):
  #      print(end=' ')
   # for stars in range (count):
    #    print ("*", end=' ')
    #space_count = space_count - 1
    #count = count + 1

    #print()

    # Function to demonstrate printing pattern of numbers 
def numpat(n): 
      
    # initialising starting number  
    num = 1
  
    # outer loop to handle number of rows 
    for i in range(0, n): 
      
        # re assigning num 
        num = 1
      
        # inner loop to handle number of columns 
            # values changing acc. to outer loop 
        for j in range(0, i+1): 
          
                # printing number 
            print(num, end=" ") 
          
            # incrementing number at each column 
            num = num + 1
      
        # ending line after each row 
        print("\r") 
  
# Driver code 
n = 5
numpat(n) 
