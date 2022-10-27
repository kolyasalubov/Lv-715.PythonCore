Fibonacci1 = 1
Fibonacci2 = 1
n = int(input('Введіть число: '))

print(Fibonacci1, Fibonacci2, end =' ')
while Fibonacci2 < n:
    Fibonacci1, Fibonacci2 = Fibonacci2, Fibonacci1 + Fibonacci2
    print(Fibonacci2, end = ' ')