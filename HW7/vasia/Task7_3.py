str = input("Enter a string")
def num_characters():
    '''This function calculates the number of characters included in a given string.'''
    d={}
    for i in range(len(str)):
        d1={str[i]:str.count(str[i])}
        d.update(d1)
    print(d)
    
num_characters()
