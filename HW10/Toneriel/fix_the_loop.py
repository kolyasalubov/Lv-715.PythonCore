# Your collegue wrote an simple loop to list his favourite animals.
# But there seems to be a minor mistake in the grammar,
# which prevents the program to work. Fix it!: )

# If you pass the list of your favourite animals to the function,
# you should get the list of the animals with orderings and newlines added.

def list_animals(animals):
    '''This function returns a string with numbered new lines from each element from a list'''
    list = []
    for i in range(len(animals)):
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return ''.join(list)


animals = ['dog', 'cat', 'elephant']
print(list_animals(animals))
