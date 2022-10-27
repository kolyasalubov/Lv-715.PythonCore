# home work 6, task 1

numbers = range(1, 11)

even_numbers = []
odd_numbers = []
not_divisible_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        pass

for number in numbers:
    if number % 3 == 0 and number % 2 != 0:
        odd_numbers.append(number)
    else:
        pass

for number in numbers:
    if number % 2 != 0 and number % 3 != 0:
        not_divisible_numbers.append(number)
    else:
        pass

print(even_numbers)
print(odd_numbers)
print(not_divisible_numbers)

