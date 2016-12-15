# Gets time

import datetime

# Getting and storing user age from user

strInputDate = input("Enter your year of birth:")

# Variable for testing if the user input is a number

boolTestDigit = strInputDate.isdigit()

# A loop to test if the input is a number and print to it to screen

while True:

    # if false will print tell user the the input was a invalid

    if boolTestDigit is False:

        print("\n")

        print("That is an invalid number")

        break

        # if true will enter if block

    if boolTestDigit is True:

        # Variable for turning user input string into a integer

        intUserBirth = int(strInputDate)

        # Variable for getting current year on computer

        intYear = int(datetime.datetime.now().year)

        # Tests if user input is more then the current year if true
    
        if intUserBirth > intYear:
        # Tells user to enter number that is less then the current date
            print("\n")

            print("Plese enter a number that is less then the current date")

            break

    #Variable sets final print message by subtracting year by user input

        intUserAge = intYear - intUserBirth

    #Takes user input and turns it to string and prints the users age to screen

        strUserPrint = str(intUserAge)

        print("\n")

        print("Your age is " + strUserPrint)

        break

    #Uses input() method to pause program

input()