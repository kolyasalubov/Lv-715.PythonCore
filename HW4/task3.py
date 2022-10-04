number = int(input('number ='))
var = [0,1]

while len(var) < number and var[-1] < (number - 2):
        var.append(var[-1]+var[-2])
print(var)