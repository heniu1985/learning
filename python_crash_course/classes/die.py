from random import randint

class Die():
    """Klasa kostki do gry"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

die = Die(20)

i = 0

while i <= 10:
    die.roll_die()
    i += 1