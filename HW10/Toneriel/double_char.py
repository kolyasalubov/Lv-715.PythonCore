# Given a string, you have to return a string in which each character(case-sensitive)
# is repeated once.

def double_char(s):
    '''This function returns a string in which each character(case-sensitive) is repeated once.'''
    return ''.join([i * 2 for i in s])


print(double_char("String"))
