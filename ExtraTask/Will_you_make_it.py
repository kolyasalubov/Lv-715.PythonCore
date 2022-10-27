def make_it(m, g):
    if 25 * g >= m:
        return True
    else:
        return False


miles = 50
gallons_left = 1.5
print(make_it(m=miles, g=gallons_left))
