# You need to write a function that reverses the words in a given string. 
# A word can also fit an empty string. 
# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.


def reverse(st):
    st = st.split()             # Create a list
    st.reverse()                # Reverse the list 
    st = ' '.join(st)           # Assemble the list
    return st   

# Print the result
print(reverse("Hello. I am not God!"))


# Other version
def reverse_v2(st):
    return ' '.join(st.split()[::-1])   # [::-1] - for reversed list

# Output: God! not am I Hello.
print(reverse_v2("Hello. I am not God!"))
