from modules.helpers import clear_console

class Inventory:
    def __init__(self):
        self.coins = 100
        self.owned_weapons = []
        self.owned_potions = []

    def print(self):
        clear_console()
        if len(self.owned_weapons) == 0 and len(self.owned_potions) == 0:
            print("Nothing in inventory")
            return

        print("Weapons:")
        for index, weapon in enumerate(self.owned_weapons):
            print(f"{index + 1}. {weapon.name}")

        print("Potions:")
        for index, potion in enumerate(self.owned_potions):
            print(f"{index + 1}. {potion.name}")

        print("What would you like to do?")
        print("1. Equip Weapon")
        print("2. Consume Potion")
        print("3. Close Inventory")

        selection = input()

        match selection:
            case "1":
                # TODO
                print()
            case "2":
                # TODO
                print()
            case "3":
                return

    def add_coins(self, coins):
        self.coins += coins
        print(f"Received {coins} coins")

    def add_weapon(self, weapon):
        self.owned_weapons.append(weapon)
        print(f"Added {weapon.name} to inventory")

    def add_potion(self, potion):
        self.owned_potions.append(potion)
        print(f"Added {potion.name} to inventory")

