# chickens=2
# cows=4
# pigs=4
# chic=int(input("enter the no of chickens:"))
# cows1=int(input("enter the no of cows: "))
# pigs1=int(input("enter the no of pig: "))



# def animals(chickens, cows, pigs):
#     return chic*chickens+cows1*cows+pigs1*pigs
# print(animals(chickens,cows,pigs))

def number_of_legs(chickens, cows, pigs):

    legs = (2 * chickens) + (4 * cows) + (4 * pigs)

    return legs


# print the number of legs for each set of input

print(number_of_legs(2, 3, 5))
print(number_of_legs(1, 2, 3))
print(number_of_legs(5, 2, 8))
print(number_of_legs(10, 3, 4))
print(number_of_legs(11, 21, 32))
print(number_of_legs(2, 8, 8))
print(number_of_legs(0, 1, 1))