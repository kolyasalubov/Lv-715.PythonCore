# home work 7, task 3

from itertools import count

def count_characters(string: str) -> dict:
    """This function calculates the number of characters included in a given string"""

    characters_counted = {}
    unique_characters = set(string)

    for character in unique_characters:
        characters_counted[character] = string.count(character)

    return characters_counted
        
print(count_characters("hello"))