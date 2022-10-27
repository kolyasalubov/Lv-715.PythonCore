def count_sheep(sheep):
    d = {}
    for i in sheep:
        if i not in d:
            d[i] = 0
        d[i] = d[i] + 1
    return d


sheep = [True, True, True, False,
         True, True, True, True,
         True, False, True, False,
         True, False, False, True,
         True, True, True, True,
         False, False, True, True]

print(count_sheep(sheep=sheep)[False])
