# Your collegue wrote a simple loop to list his favourite animals. 
# But there seems to be a minor mistake in the grammar, which prevents the program to work. 
# Fix it! :)

# If you pass the list of your favourite animals to the function, 
# you should get the list of the animals with orderings and newlines added.


from logging.config import listen


def list_animals(animals):
    list = ''
    for i in range(len(animals)):                       #cannot use just range(anumals), need to know the length
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return list


animals = [ 'dog', 'cat', 'elephant' ]

print(list_animals(animals))