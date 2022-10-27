# 1
num = 9518
num = str(num)
p = int(num[0]) * int(num[1]) * int(num[2]) * int(num[3])
print(p)

# 2
num = 9518
thousand = num // 1000
hundred = num // 100 % 10
tens = num // 10 % 10
one = num % 10
p = thousand * hundred * tens * one
print(p)

num = 9518
num = str(num)
reverse = num[::-1]
reverse = int(reverse)
print(reverse)

num = 9518
num = list(str(num))
num.sort()
num = ''.join(num)
num = int(num)
print(num)