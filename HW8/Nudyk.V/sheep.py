# Consider an array/list of sheep where some sheep may be missing from their place. 
# We need a function that counts the number of sheep present in the array (true means present).

def count_sheeps(sheep):
    ''' Counts the ammount of sheep inside a list'''
    
    return sheep.count(True)
    

print(count_sheeps([True, False, 1, None, 10>9, 0]))
