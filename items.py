import random

class Sword():
    def __init__(self):
        self.item_type = "Weapon"
        self.item_rarity = self.generate_item_rarity()
        self.name = self.generate_name()
    
    def generate_name(self):
        prefix = ["Hatchion", "Sabre", "Broadsword", "Cutlass", "Claymate", "Katana"]
        middle = " of the "
        suffix = ["Boar", "Bear", "Tiger", "Monkey", "Eagle", "Crocodile"]

        name = prefix[random.randrange(len(prefix))] + middle + suffix[random.randrange(len(suffix))]
        return name
    
    def generate_item_rarity(self):
        rarity_tier = ["Common", "Uncommon", "Rare", "Epic"]

        rarity = rarity_tier[random.randrange(len(rarity_tier))]
        return rarity
    
    def __str__(self):
        return self.name

class Potion():
    def __init__(self):
        self.item_type = "Consumable"
        self.name = self.generate_name()
        
    def generate_name(self):
        potion_type = ["Health", "Mana", "Strength", "Stamina", "Agility", "Intelligence"]

        name = potion_type[random.randrange(len(potion_type))] + " potion"
        return name

    def __str__(self):
        return self.name

class Chestpiece():
    def __init__(self):
        self.item_type = "Armor"
        self.item_rarity = self.generate_item_rarity()
        self.name = self.generate_name()
    
    def generate_name(self):
        suffix = ["Boar", "Bear", "Tiger", "Monkey", "Eagle", "Crocodile"]

        name = "Chestplate of the " + suffix[random.randrange(len(suffix))]
        return name

    def generate_item_rarity(self):
        rarity_tier = ["Common", "Uncommon", "Rare", "Epic"]

        rarity = rarity_tier[random.randrange(len(rarity_tier))]
        return rarity

    def __str__(self):
        return self.name
