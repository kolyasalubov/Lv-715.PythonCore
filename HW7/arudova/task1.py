def sorting(x,y):
    """This function returns bigger value"""
    if x > y:
        print(f'{x} bigger')
    elif y > x:
        print(f'{y} bigger') 
    else:
        return 'the numbers are equial'
val_1 = int(input()) 
val_2 = int(input())
print(sorting(val_1,val_2))