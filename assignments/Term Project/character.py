import random

class Character:
    def __init__(self):
        # Initialize combat_strength and health_points with random values
        self._combat_strength = random.randint(10, 20)
        self._health_points = random.randint(50, 100)

    @property
    def combat_strength(self):
        # Return the private attribute _combat_strength
        return self._combat_strength

    @combat_strength.setter
    def combat_strength(self, value):
        # Set the value of the private attribute _combat_strength
        self._combat_strength = value

    @property
    def health_points(self):
        # Return the private attribute _health_points
        return self._health_points

    @health_points.setter
    def health_points(self, value):
        # Set the value of the private attribute _health_points
        self._health_points = value