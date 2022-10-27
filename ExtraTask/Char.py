def double_char(s):
    result = ""
    for i in s:
        result += i * 2
    return result


assert double_char("String") == "SSttrriinngg"
assert double_char("Hello World") == "HHeelllloo  WWoorrlldd"
assert double_char("1234!_ ") == "11223344!!__  "
