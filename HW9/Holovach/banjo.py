def are_you_playing_banjo(name):

    if name[0] == 'R' or name[0] == 'r':
        name = name + " plays banjo"
    else:
        name = name + " does not play banjo"

    return name

print(are_you_playing_banjo("Rocki"))
print(are_you_playing_banjo("rocki"))
print(are_you_playing_banjo("Pocki"))
print(are_you_playing_banjo("mocki"))