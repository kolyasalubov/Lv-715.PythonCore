# Create a class Ghost

# Ghost objects are instantiated without any arguments.

# Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or
# "red" when instantiated

from random import choice


class Ghost(object):

    def __init__(self):
        self.color = choice(['white', 'yellow', 'purple', 'red'])


ghost = Ghost()
print(ghost.color)
