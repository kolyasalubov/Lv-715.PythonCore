from concurrent.futures import process
from itertools import count


def calc_number_of_char_in_string(str: str) -> dict:

    """
    Calculate the number of characters included in a given string
    """

    ordered_set = sorted(set(str))

    dict_with_char_and_their_amounts = {}

    for x in ordered_set:
        dict_with_char_and_their_amounts[x] = str.count(f"{x}")

    return dict_with_char_and_their_amounts


print(calc_number_of_char_in_string(input("Enter characters:")))