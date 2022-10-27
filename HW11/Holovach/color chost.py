import random


class Ghost(object):

    def __init__(self) -> None:
        self.color = random.choice(["white", "yellow", "purple", "red"])

    # def color(self):
    #     return random.choice(["white", "yellow", "purple", "red"])

print(Ghost().color)
