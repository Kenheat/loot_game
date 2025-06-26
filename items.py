import random

class Sword():
    def __init__(self):
        self.item_type = "Weapon"
        self.damage_per_second = 3
        self.name = self.generate_name()
    
    def generate_name(self):
        prefix = ["Greatsword", "Sword", "Broadsword", "Cutlass", "Shortsword", "Katana"]
        middle = " of the "
        suffix = ["Boar", "Bear", "Tiger", "Monkey", "Eagle", "Crocodile"]

        name = prefix[random.randrange(0, 6)] + middle + suffix[random.randrange(0, 6)]

        return name
    
    def __str__(self):
        return self.name