# In the range from 1 to 10 determine
# • even numbers that are divisible by 2,
# • odd numbers, which are divisible by 3,
# • numbers that are not divisible by 2 and 3.

# Create empty lists for out results
even_nums = []     
odd_nums = []
else_nums = []

# Loop for the nums in range from 1 to 10 (in code from 1 to 11 to include '10')
for num in range(1,11):
    if num % 2 == 0:                        # for nums divisible by 2
        even_nums.append(num)
    elif num % 2 != 0 and num % 3 == 0:     # for nums divisible by 3
        odd_nums.append(num)
    else:                                   # for the nums that are left
        else_nums.append(num)

# Print the results
print('These numbers are divisibe by two:', *even_nums)
print('These numbers are divisible by three:', *odd_nums)
print('These numbers do not divide by tow or three:', *else_nums)