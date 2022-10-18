# Given a string, you have to return a string in which 
# each character (case-sensitive) is repeated once.


def double_char(string):
    '''
    Returns a string with all charecters doubled 
    '''
    new_string = []
    string = list(string)
    for char in string:
        char = char * 2
        new_string.append(char)

    return ''.join(new_string)

print(double_char('1234!_ '))
print(double_char('Hello'))
print(double_char('Hello World!'))
print(double_char('Why does it not work ???'))




def double_char_2(string):
    '''
    A simplified version on double_char
    '''
    return (''.join(char * 2 for char in string))

print(double_char_2('1234!_ '))
print(double_char_2('Hello'))
print(double_char_2('Hello World!'))
print(double_char_2('Why does it not work ???'))


