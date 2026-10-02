class Potion:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

class StrengthPotion(Potion):
    def __init__(self, strength):
        self.strength = strength

class VitalityPotion(Potion):
    def __init__(self, vitality):
        self.vitality = vitality
