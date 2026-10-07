import json
from modules.helpers import clear_console

class Room():
    def __init__(self, name, floor, enemy, lootable_coins, lootable_potion):
        self.name = name
        self.floor = floor
        self.enemy = enemy
        self.enemy_defeated = False
        self.lootable_coins = lootable_coins
        self.lootable_potion = lootable_potion

    def intro(self):
        with open("dialogues/rooms.json", "r") as file:
            data = json.load(file)

        print(data[self.name])
        input()


    def loot(self, inventory, main_menu):
        clear_console()
        if self.lootable_coins is None and self.lootable_potion is None:
            print("The room is empty")

        if self.lootable_coins is not None:
            print(f"You found {self.lootable_coins} coins")
            inventory.add_coins(self.lootable_coins)
            self.lootable_coins = None

        if self.lootable_potion is not None:
            print(f"You found {self.lootable_potion.name}")
            inventory.add_potion(self.lootable_potion)
            self.lootable_potion = None

        input("Press any key to continue...")
        main_menu()

