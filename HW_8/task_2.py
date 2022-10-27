import string


def is_valid_pass(password):
    kol_lowercase = 0
    kol_uppercase = 0
    kol_digit = 0
    kol_character = 0
    for i in password:
        if i in string.ascii_lowercase:
            kol_lowercase += 1
        if i in string.ascii_uppercase:
            kol_uppercase += 1
        if i.isdigit() == True:
            kol_digit += 1
        if i in "$#@":
            kol_character += 1

    if kol_lowercase == 0 or kol_uppercase == 0 or kol_digit == 0 or kol_character == 0:
        return False

    if len(password) < 6 or len(password) > 16:
        return False

    return True


def is_valid_pass_v2(password):
    if sum(map(str.islower, password)) == 0:
        return False
    if sum(map(str.isupper, password)) == 0:
        return False
    if sum(map(str.isdigit, password)) == 0:
        return False
    if "@" not in password and "#" not in password and "$" not in password:
        return False
    if len(password) < 6 or len(password) > 16:
        return False
    return True


p = input()
if is_valid_pass_v2(p) == True:
    print("All OK")
else:
    print("Error")
