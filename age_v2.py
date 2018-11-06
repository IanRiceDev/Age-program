# Gets time
import sys
import datetime

user_birth_year = input("Enter your year of birth:")

get_year = int(datetime.datetime.now().year)

test_for_digit = user_birth_year.isdigit()

if test_for_digit is False:

    print("That is an invalid number")
    print("Terminating program")
    input()
    sys.exit()

elif test_for_digit is True:

    result = get_year - int(user_birth_year)
    print(result)
    input()
