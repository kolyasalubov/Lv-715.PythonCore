FournumVariable = 9612
x = [int(a) for a in str(FournumVariable)]
print(x)
productNum = x[0] * x[1] * x[2] * x[3]
print("Добуток цифр ",productNum) 
print ("Реверс",x[3], x[2], x[1], x[0])
x.sort()

print("сортування",x)