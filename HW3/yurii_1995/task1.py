# home work 3, task 1, part 1

# input data

with open('ZenExample.txt', 'r') as file_of_zen:
    content = file_of_zen.read()

def word_counter(word:str):
    """This function is for looking for a user's word. It returns amount of that in the file of Zen"""
    word_counter = 0
    for word_to_find in content.split():
        if word_to_find == word:
            word_counter += 1

    return word_counter

# results
amount_of_better = word_counter("better")
amount_of_never = word_counter("never") + word_counter("never.")
amount_of_is = word_counter("is")

print(amount_of_better)
print(amount_of_never)
print(amount_of_is)

# home work 3, task 1, part 2

upper_content = content.upper()
print(upper_content)

# home work 3, task 1, part 3

replace_content = content.replace("i", "&")
print(replace_content)