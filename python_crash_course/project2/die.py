from random import randint

class Die():
    """Klasa przedstawiająca pojedynczą kość do gry"""

    def __init__(self, num_sides=6):
        """Określenie domyślnej liczby ścian kości na 6."""
        self.num_sides = num_sides

    def roll(self):
        """Rzut kością."""
        return randint(1, self.num_sides)