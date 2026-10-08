from modules.helpers import clear_console, enter_break, invalid_selection

class Inventory:
    def __init__(self, coins, owned_weapons, owned_potions):
        self.coins = coins
        self.owned_weapons = owned_weapons
        self.owned_potions = owned_potions

    def print(self, player, main_menu):
        clear_console()
        print(f"Coins: {self.coins}")
        if len(self.owned_weapons) == 0 and len(self.owned_potions) == 0:
            print("Nothing in inventory")
            enter_break()
            return main_menu()

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
                self.equip_weapon(player, main_menu)
            case "2":
                self.consume_potion(player, main_menu)
            case "3":
                return main_menu()
            case _:
                return invalid_selection(lambda: self.print(player, main_menu))

    def add_coins(self, coins):
        self.coins += coins
        print(f"Added {coins} coins to inventory")

    def add_weapon(self, weapon):
        self.owned_weapons.append(weapon)
        print(f"Added {weapon.name} to inventory")

    def add_potion(self, potion):
        self.owned_potions.append(potion)
        print(f"Added {potion.name} to inventory")

    def equip_weapon(self, player, main_menu):
        clear_console()
        choice_amount = 0
        print("Which weapon would you like to equip?")
        for index, weapon in enumerate(self.owned_weapons):
            choice_amount += 1
            print(f"{index + 1}. {weapon.name}")

        print(f"{choice_amount + 1}. Go back")

        selection = input()

        try:
            int(selection)
        except:
            return invalid_selection(lambda: self.equip_weapon(player, main_menu))

        if 1 <= int(selection) <= choice_amount:
            self.owned_weapons.append(player.equipped_weapon)
            player.equipped_weapon = self.owned_weapons[int(selection) - 1]
            self.owned_weapons.pop(int(selection) - 1)
            return main_menu()
        elif int(selection) == choice_amount + 1:
            return self.print(player, main_menu)
        else:
            return invalid_selection(lambda: self.equip_weapon(player, main_menu))


    def consume_potion(self, player, main_menu):
        clear_console()
        choice_amount = 0
        print("Which potion would you like to consume?")
        for index, potion in enumerate(self.owned_potions):
            choice_amount += 1
            print(f"{index + 1}. {potion.name}")

        print(f"{choice_amount + 1}. Go back")

        selection = input()

        try:
            int(selection)
        except:
            return invalid_selection(lambda: self.consume_potion(player, main_menu))

        if 1 <= int(selection) <= choice_amount:
            selection_name = self.owned_potions[int(selection) - 1].name
            player.has_strength_effect = True
            self.owned_potions.pop(int(selection) - 1)
            return main_menu()
        elif int(selection) == choice_amount + 1:
            return self.print(player, main_menu)
        else:
            invalid_selection(lambda: self.consume_potion(player, main_menu))
