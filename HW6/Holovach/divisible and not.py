divisible_by_2 = []
divisible_by_3 = []
not_divisible_by_2_and_3 = []

# for x in range(1,10):
#     if x%2 == 0:
#         divisible_by_2.append(x)
#     elif x%3 == 0:
#         divisible_by_3.append(x)
#     else:
#         not_divisible_by_2_and_3.append(x)

for x in range(1,10):
    if x%2 == 0:
        divisible_by_2.append(x)
    if x%3 == 0:
        divisible_by_3.append(x)
    if x%2 != 0 and x%3 != 0:
        not_divisible_by_2_and_3.append(x)

print(f"""After operation:
        divisible by 2 - {divisible_by_2}; 
        divisible by 3 - {divisible_by_3};
        not divisible by 2 and 3 - {not_divisible_by_2_and_3}.
        """) 