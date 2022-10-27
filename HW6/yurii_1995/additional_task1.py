# class work 6, task 1 (using by min and max funcs)

numbers = []
end_number = input("Enter the end number of the list ")

for number in range(0, int(end_number)+1):
    numbers.append(number)

print(min(numbers))
print(max(numbers))

# class work 6, task 1 (using by sorting algorithm)

for number in range(1, int(end_number)+1):
    min_number = 0
    max_number = 0
    numbers.append(number)

    if number < min_number:
        min_number = number
    elif number > max_number:
        max_number = number

print(min_number)
print(max_number)