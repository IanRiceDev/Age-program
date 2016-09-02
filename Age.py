import datetime

strInputDate = input("Enter your year of birth:")

boolTestDigit = strInputDate.isdigit()

while True:
    if boolTestDigit is False:

        print("\n")

        print("That is not a number")

        break

    if boolTestDigit is True:

        intUserBirth = int(strInputDate)

        intYear = int(datetime.datetime.now().year)

        if intUserBirth > intYear:

            print("\n")

            print("Plese enter a number that is less then the current date")

            break

        intUserAge = intYear - intUserBirth

        strUserPrint = str(intUserAge)

        print("\n")

        print("Your age is " + strUserPrint)

        break

input()