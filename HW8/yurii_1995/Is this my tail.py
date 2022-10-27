# Is this my tail?

def correct_tail(body, tail):
    sub = body[-1].find(tail)
    
    if sub == -1:
        return False
    else:
        return True