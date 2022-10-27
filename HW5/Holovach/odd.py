for x in range(200):
    if x % 2 != 0 and x < 100:
        print(x, end  = " - ")

print("")
print("")

for x in range(200):
    if x % 2 == 0 or x >= 100:
        continue
    print(x, end  = " - ")  