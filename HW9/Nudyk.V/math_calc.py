def adding(*arg):
    ''' Returns a total of the sum of given numbers
    '''

    total = 0
    for number in arg:
        total += number
    return total

def substract(*arg):
    ''' Returns a total of substraction of the given numbers
    '''

    total = arg[0] - sum(arg[1:])
    return total
    

def multiply(*arg):
    ''' Returns a total of multiplication of the given numbers
    '''

    total = 1
    for number in arg:
        total *= number
    return total

def divide(*arg):
    ''' Returns a total of division of the given numbers
    '''
    
    total = arg[0]
    for number in arg[1:]:
        total /= number
    return total