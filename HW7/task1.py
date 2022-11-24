from random import randint

def largest_number(first, second):

    if first > second:
        return first
    else:
        return second

first = randint(1, 1000)
second = randint(1, 1000)

print(f"The first number is {first}")
print(f"The second number is {second}")
print(f"The largest number is {largest_number(first, second)}")