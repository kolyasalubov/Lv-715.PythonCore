# Write a script that checks the login that the user enters.
# If the login is "First", then greet the users. If the login is
# different, send an error message.
# (need to use loop while)


while True:
    user_login = input('Enter your login: ')      
    if user_login == 'First':
        print(f'Hello, {user_login} user !')
        break
    else:
        print('Error: enter correct login !')

# No comments