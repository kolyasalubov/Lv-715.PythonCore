# Complete the method that takes a boolean value and 
# return a "Yes" string for true, or a "No" string for false.


def bool_to_word(boolean):
    ''' Return a positive answer 'Yes' if the boolean value is True and
        'No' if the boolean value is False'''

    return ('Yes' if boolean == True else 'No')

# Some tests
print(bool_to_word(None))
print(bool_to_word(1))
print(bool_to_word(False))
print(bool_to_word({}))
print(bool_to_word(5 > 4))