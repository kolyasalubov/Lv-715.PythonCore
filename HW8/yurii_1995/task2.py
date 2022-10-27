# home work 8, task 2

import string

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
spec_characters = ["$", "#", "@"]
upper_alphabet = list(string.ascii_uppercase)
lower_alphabet = list(string.ascii_lowercase)

ask_user = True

def validation_user_password(user_pass: str, characters: list):
    """This function accepts user password as str for validation, characters list to match with user pass,
     and returns True if at least one character from the given characters is found, False - otherwise.
     """
    validation_list = []
    for character in characters:
        if character in user_pass:
            validation_list.append(character)
    if validation_list:
        return True
    else:
        return False

while ask_user:
    user_pass = input("Please type your password here: ")

    # check inputted password

    if len(user_pass) < 6:
        print("Your password must be more then 6 characters")
    elif len(user_pass) > 16:
        print("Your password must be less then 16 characters")
    else:
        if not validation_user_password(user_pass, numbers):
            print("Your password must contains one digit character (1-9) at least")
        elif not validation_user_password(user_pass, spec_characters):
            print("Your password must contains one special character ($, #, @) at least")
        elif not validation_user_password(user_pass, upper_alphabet):
            print("Your password must contains one letter in uppper case (A-Z) at least")
        elif not validation_user_password(user_pass, lower_alphabet):
            print("Your password must contains one letter in lower case (a-z) at least")
        else:
            print("Your password is correct and saved successfully")
            ask_user = False

                                  

