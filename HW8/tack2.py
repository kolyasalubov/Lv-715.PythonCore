import re 

password = input('Пароль має містити від 10 до 20 символів, включаючи принаймні 1 малу літеру, 1 велику літеру, 1 цифру та принаймні 1 символ -$,#,@: ')

def validate_password(password):
    """Returns True only if password is strong enough."""
    Value=r'[A-Z|a-z|0-9|.$#@]{10,20}'
    match = re.fullmatch(Value, password)
    if bool(password) == True:
        return 'Дякую. Ваш пароль дійсний'
    else:
        return 'Ваш пароль неправильний. Спробуйте знову.'
    
print(validate_password(password))