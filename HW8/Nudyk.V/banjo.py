# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

#  The function takes a name as its only argument, and returns one of the following strings:
# name + " plays banjo" 
# name + " does not play banjo"

print('Are you playing banjo?')

def are_you_playing_banjo(name):
    ''' Checks if the name starts with 'R' or 'r'. If does, that return name + " plays banjo".
        If not returns name + " does not play banjo"'''
        
    if name[0] == 'R' or name[0] == 'r':
        return (f'{name} plays banjo')
    else:
        return (f'{name} does not play banjo')

print(are_you_playing_banjo('volodia'))
print(are_you_playing_banjo('romeo'))

