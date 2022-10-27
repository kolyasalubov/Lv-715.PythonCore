# Write a function that calculates the number of characters
# included in a given string
# • input: "hello"
# • output: {"h":1, "e":1,"l":2,"o":1}


def nums_of_char(text):
    # Created an empty dictionary
    text_dict = {} 
    # Changed the type of the text into list
    text = list(text)
    # Loop for every char to get it counted
    for char in text:
        text_dict[char] = text.count(char)
    return text_dict

print(nums_of_char("hello"))

