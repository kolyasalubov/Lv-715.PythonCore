def correct_tail(body, tail):
    
    sub = body[len(body)-len(tail):]
        
    if sub == tail:
        return True
    else:
        return False

    # return body.endswith(tail)

print(correct_tail("Fox", "x"))