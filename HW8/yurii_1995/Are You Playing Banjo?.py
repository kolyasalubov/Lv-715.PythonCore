# Are You Playing Banjo?

def are_you_playing_banjo(name):
    find_R = name.find("R")
    find_r = name.find("r")
    
    if find_R == 0:
        name = f"{name} plays banjo"
        return name
    elif find_r == 0:
        name = f"{name} plays banjo"
        return name
    else:
        name = f"{name} does not play banjo"
        return name