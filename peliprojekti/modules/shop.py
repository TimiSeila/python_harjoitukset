from modules.weapon import Weapon
from modules.helpers import clear_console, enter_break, invalid_selection
from modules.potion import StrengthPotion

class Shop:
    def __init__(self, available_weapons):
        self.available_weapons = available_weapons
        self.available_potions = [StrengthPotion(), StrengthPotion(), StrengthPotion()]

    def print(self, player, main_menu):
        clear_console()
        print("What would you like to buy?")
        print("1. Weapons")
        print("2. Potions")

        selection = input()

        match selection:
            case "1":
                self.print_weapons(player, main_menu)
            case "2":
                self.print_potions(player, main_menu)
            case _:
                return invalid_selection(main_menu)

    def print_weapons(self, player, main_menu):
        clear_console()
        print("Which weapon would you like to buy?")
        choice_amount = 0

        for index, weapon in enumerate(self.available_weapons):
            choice_amount += 1
            print(f"{index + 1}. {weapon.name}")
            print(f"Damage: {weapon.damage}, Cost: {weapon.cost}")

        selection = input()

        try:
            int(selection)
        except:
            return invalid_selection(main_menu)

        if 1 <= int(selection) <= choice_amount:
            self.buy_weapon(int(selection) - 1, player, main_menu)
        else:
            return invalid_selection(main_menu)

    def print_potions(self, player, main_menu):
        clear_console()
        print("Which potion would you like to buy?")
        choice_amount = 0

        for index, potion in enumerate(self.available_potions):
            choice_amount += 1
            print(f"{index + 1}. {potion.name}")
            print(f"Strength: {potion.strength}, Cost: {potion.cost}")

        selection = input()

        try:
            int(selection)
        except:
            return invalid_selection(main_menu)

        if 1 <= int(selection) <= choice_amount:
            self.buy_potion(player, main_menu)
        else:
            return invalid_selection(main_menu)
        

    def buy_weapon(self, index, player, main_menu):
        weapon = self.available_weapons[index]

        if weapon.cost > player.inventory.coins:
            print("Not enough coins")
            enter_break()
            return main_menu()

        player.inventory.coins -= weapon.cost
        player.inventory.add_weapon(weapon)
        self.available_weapons.pop(index)
        return main_menu()

    def buy_potion(self, player, main_menu):
        potion = self.available_potions[0]

        if potion.cost > player.inventory.coins:
            print("Not enough coins")
            enter_break()
            return main_menu()

        player.inventory.coins -= potion.cost
        player.inventory.add_potion(potion)
        self.available_potions.pop(0)
        return main_menu()
