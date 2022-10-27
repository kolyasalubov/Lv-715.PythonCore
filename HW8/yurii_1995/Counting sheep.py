# Counting sheep...

def count_sheeps(sheeps):
    counter = 0
    for sheep in sheeps:
        if sheep:
            counter += 1
        elif not sheep:
            continue
        else:
            break
        
    return counter