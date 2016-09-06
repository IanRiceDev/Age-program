# Gets time

import datetime

# Getting and storing user age from user

strInputDate = input("Enter your year of birth:")

# Var for testing if the user imput is a number

boolTestDigit = strInputDate.isdigit()

# A loop to test if the input is a number and print to it to screen

while True:
   
   # if false will print tell user the the input was a letter and not a number
   
   if boolTestDigit is False:

        print("\n")

        print("That is not a number")

        break
    
	# if true will enter if block
   
   if boolTestDigit is True:
        
		# Var for turning user input str into a int
        
		intUserBirth = int(strInputDate)
        
		# Var for getting current year on monitor
        
		intYear = int(datetime.datetime.now().year)
        
		# Tests if user input is more then the currant year if true       
		# Tells user to enter number that is less then the currant date
        
		if intUserBirth > intYear:

            print("\n")

            print("Plese enter a number that is less then the current date")

            break
        
		#Var sets final print message by subtrating year by user input
        
		intUserAge = intYear - intUserBirth
        
		#Takes user input and turns it to string and prints the users age to screen
        
		strUserPrint = str(intUserAge)

        print("\n")

        print("Your age is " + strUserPrint)

        break

#Uses input() method to pasue program

input()
