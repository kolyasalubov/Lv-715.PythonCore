# Open Zen file
from posixpath import split


zen = open("ZenExample.txt")

# Turn zen's content into one string 
content = zen.read()
content_into_string = content.replace("\n", " ")
# print(repr(a))                        # show content with hiden symbols
print(id(content))                      # value's id
print(type(content))
print(id(content_into_string))          # another object after values' method execution
print(type(content_into_string))
print(content_into_string)

# Find number of including "better", "never" and "is" in zen
#
# number_of_better = content_into_string.count("better")
# number_of_never = content_into_string.count("never")
# number_of_is = content_into_string.count("is")

splitted_content = content_into_string.split()
print(splitted_content)
print(type(splitted_content))
number_of_better = 0
number_of_never = 0
number_of_is = 0
for i in splitted_content:
    if "better" in i:
        number_of_better += 1
    if "never" in i:
        number_of_never += 1
    if "is" in i:
        number_of_is += 1
print(f"The words - 'better' {number_of_better} times and 'never' {number_of_never} times and 'is' {number_of_is} times were found in Zen file")

# Content into uppercase
print(content_into_string.upper())

# Replace "i" with "&"
print(content_into_string.replace("i", "&"))

zen.close()


# Fourth-digit numbers handling
#
# Multiplication of every sign sequencently
four_digit_number = input("Enter four-digit number:")

multiplication = 1

for y in four_digit_number:
    multiplication *= int(y)
print(f"Multiplication of every sign sequencently is {multiplication}")

# Reverse order of digits
reversed_four_digit_number_in_string = "".join(reversed(four_digit_number))
print(f"Reversed order of digits - {reversed_four_digit_number_in_string}")

# Sort digits' sequence
sorted_sequence = "".join(sorted(four_digit_number))
print(f"Sorted digits' sequence - {sorted_sequence}")


# Exchange values between two variables 
#
# 1

one = int(input("Enter value 'One':"))
two = int(input("Enter value 'Two':"))

one = one + two 
two = one - two 
one = one - two 

print(f"One = {one}") 
print(f"Two = {two}") 

# 2 

one, two = two, one

print(f"One = {one}") 
print(f"Two = {two}") 
