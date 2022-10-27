def double_char(s):
    return ''.join([x+x for x in s])

print(double_char("Hello World"))
print(double_char("1234!_ "))