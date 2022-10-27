# Write a function taking in a string like
#     WOW this is REALLY          amazing
# and returning
#     Wow this is really amazing.
# String should be capitalized and properly spaced. Using re and string is not allowed.

user_input = input('Write some nonsense:')

def filter_words(st):
    # Firsly making all the words lowercase and the first char uppercase
    st = st.lower().capitalize()      
    # Then spliting the strings into a list so getting rid of the spaces
    st = st.split()
    # Assembling the list with a space between the words
    st = ' '.join(st)
    return st


print(filter_words(user_input))


# or I can try to write it in one line

def filter_words_v2(str):
    return ' '.join(str.lower().capitalize().split())


print(filter_words_v2(user_input))


