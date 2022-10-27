# home work 5, task 1

numbers = [1, 3, 6, 67, 445, 3445, 8, 433, 1000]

numbers_copy = numbers.copy()
del numbers[:]

for number in numbers_copy:
    numbers.append(float(number))

print(numbers)