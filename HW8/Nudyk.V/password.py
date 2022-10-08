import re


def password(user_input):
    ''' Checks if the password is valid
    '''

    if  re.findall('[a-z]', user_input) == [] or\
    re.findall('[A-Z]', user_input) == [] or\
    re.findall('[0-9]', user_input) == [] or\
    re.findall('[$,#,@]', user_input) == [] or\
    len(user_input) < 6 or\
    len(user_input) > 16:
        return 'Bad password, pal'
    else:
        return 'Very good password, hacker'



print(password('a'))
print(password('aZ'))
print(password('aZ1'))
print(password('aZ1@'))
print(password('aZ1@aZ1@'))