# home work 3, task 2, part 1 (product of number)

number = 4587 # input data

str_number = str(number)

digit_1 = int(str_number[0])
digit_2 = int(str_number[1])
digit_3 = int(str_number[2])
digit_4 = int(str_number[3])

product_numbers = digit_1 * digit_2 * digit_3 * digit_4
print(f"Product of number {number} is {product_numbers}")

# home work 3, task 2, part 2 (numbers reverse)

list_numbers = []
list_numbers.append(digit_1)
list_numbers.append(digit_2)
list_numbers.append(digit_3)
list_numbers.append(digit_4)

rev_number = str_number[::-1]
print(f"The {number} in reverse order is {rev_number}")

# home work 3, task 2, part 3 (sort of numbers)

print(sorted(list_numbers))