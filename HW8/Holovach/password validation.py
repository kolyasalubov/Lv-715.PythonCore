import re

def password_validation():

    while 1:

        password = input("Enter the password:")

        if len(password) < 6:
            print("Your password's length should be more than 6 characters!")
            continue
        elif len(password) > 16:
            print("Your password's length should be less than 16 characters!")
            continue
        elif bool(re.findall("[a-z]", password)) != True:
            print("Your password has to contain a sign from this range[a-z]!")
            continue
        elif bool(re.findall("[A-Z]", password)) != True:
            print("Your password has to contain a sign from this range[A-Z]!")
            continue
        elif bool(re.findall("[0-9]", password)) != True:
            print("Your password has to contain a number from this range[0-9]!")
            continue
        elif bool(re.findall("[$,#,@]", password)) != True:
            print("Your password has to contain a sign from this range[$,#,@]!")
            continue
        else:
            return "You are welcome!"
    
    
             
print(password_validation())
