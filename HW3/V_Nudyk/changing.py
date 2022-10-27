number_a = int(input("Give me a number that I will store as a: "))
number_b = int(input("Give me another number that I will recognize as b: "))

print("a =", number_a)
print("b =", number_b)

print("Now lets change the two numbers between themselves: ")

#The task is to change the nums without the third var
number_a, number_b = number_b, number_a

print("a =", number_a, "\nand \nb =", number_b)
