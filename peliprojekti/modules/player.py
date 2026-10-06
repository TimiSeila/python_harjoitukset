from modules.inventory import Inventory
from modules.weapon import Weapon

class Player:
    def __init__(self, name, max_health):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.inventory = Inventory()
        self.equipped_weapon = Weapon("Wooden Sword", 12, 10)
        self.has_strength_effect = false
        self.has_vitality_effect = false
