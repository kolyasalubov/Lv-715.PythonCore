import re
password = input('password = ')

if bool(re.match(r'\w*[A-Z]\w*', password)) is False:
    print('at least 1 Uppercase')
elif bool(re.match(r'\w*[0-9]\w*', password)) is False:
    print('at least one number')
elif bool(re.match(r'\w*["$","#","@"]\w*', password)) is False:
    print('at least one sign')
elif 7 < len(password) < 17:
    print(password)
else:
    print('password must include from 6 to 17 characters')