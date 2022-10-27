def list_animals(animals):
    list = ''
    for i in range(len(animals)):
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return list


animals = ['dog', 'cat', 'elephant']
assert list_animals(animals) == '1. dog\n2. cat\n3. elephant\n'
