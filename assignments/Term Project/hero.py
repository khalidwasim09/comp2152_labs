from character import Character
import random

class Monster(Character):
    def __init__(self):
        # Initialize the Monster using the parent class's constructor
        super().__init__()
        self._name = "Monster"  # Set the name of the Monster

    def monster_attacks(self):
        # Monster performs an attack, returning a random value for attack strength
        attack_value = random.randint(5, 15)
        print(f"{self._name} attacks with strength {attack_value}")
        return attack_value

    def __del__(self):
        # Call the parent destructor
        super().__del__()
        print("The Monster object is being destroyed by the garbage collector")