class Player:
    def __init__(self, name, max_health, current_health, inventory, equipped_weapon, has_strength_effect):
        self.name = name
        self.max_health = max_health
        self.current_health = current_health
        self.inventory = inventory
        self.equipped_weapon = equipped_weapon
        self.has_strength_effect = has_strength_effect
