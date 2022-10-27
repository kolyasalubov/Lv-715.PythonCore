# home work 8, task 2 (using regular expression)

import re

ask_user = True         

while ask_user:
    user_pass = input("Please type your password here: ")

    # check inputted password

    if len(user_pass) < 6:
        print("Your password must be more then 6 characters")
    elif len(user_pass) > 16:
        print("Your password must be less then 16 characters")
    elif not re.findall("\d", user_pass):
        print("Your password must contains one digit character (0-9) at least")
    elif not re.findall("[@#$]", user_pass):
        print("Your password must contains one special character ($, #, @) at least")
    elif not re.findall("[A-Z]", user_pass):
        print("Your password must contains one letter in uppper case (A-Z) at least")
    elif not re.findall("[a-z]", user_pass):
        print("Your password must contains one letter in lower case (a-z) at least")
    else:
         print("Your password is correct and saved successfully")
         ask_user = False