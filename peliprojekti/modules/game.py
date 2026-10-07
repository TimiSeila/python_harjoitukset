import json
from modules.player import Player
from modules.room import Room
from modules.helpers import clear_console
from modules.weapon import Weapon
from modules.potion import StrengthPotion
from modules.enemy import Enemy
from modules.save import SaveSystem
from modules.inventory import Inventory

class Game:
    def __init__(self):
        self.save_system = SaveSystem()
        if self.save_system.has_save_file():
            player_save_data = self.save_system.load_player("save.json")
            inventory_save_data = self.save_system.load_inventory("save.json")
            intro_played_save_data = self.save_system.load_intro_played("save.json")
            highest_unlocked_floor_save_data = self.save_system.load_highest_unlocked_floor("save.json")
            room_save_data = self.save_system.load_rooms("save.json")
            current_room_index_save_data = self.save_system.load_current_room_index("save.json")
        else:
            player_save_data = self.save_system.load_player("initial_state.json")
            inventory_save_data = self.save_system.load_inventory("initial_state.json")
            intro_played_save_data = self.save_system.load_intro_played("initial_state.json")
            highest_unlocked_floor_save_data = self.save_system.load_highest_unlocked_floor("initial_state.json")
            room_save_data = self.save_system.load_rooms("initial_state.json")
            current_room_index_save_data = self.save_system.load_current_room_index("initial_state.json")

        # Initialize player from save data
        self.player = Player(
            player_save_data["name"],
            player_save_data["max_health"],
            player_save_data["current_health"],
            Inventory(
                inventory_save_data["coins"],
                [
                    Weapon(
                        weapon["name"],
                        weapon["damage"],
                        weapon["cost"]
                    ) for weapon in inventory_save_data["owned_weapons"]
                ],
                [StrengthPotion() for potion in inventory_save_data["owned_potions"]],
            ),
            Weapon(
                player_save_data["equipped_weapon"]["name"],
                player_save_data["equipped_weapon"]["damage"],
                player_save_data["equipped_weapon"]["cost"]
            ) if player_save_data["equipped_weapon"] else None,
            player_save_data["has_strength_effect"],
        )

        # Initialize game from save data
        self.intro_played = intro_played_save_data
        self.highest_unlocked_floor = highest_unlocked_floor_save_data
#       ]
        self.rooms = [
            Room(
                room["name"],
                room["floor"],
                Enemy(
                    room["enemy"]["name"],
                    room["enemy"]["max_health"],
                    room["enemy"]["attack_power"],
                    room["enemy"]["co2_emissions"],
                    room["enemy"]["coin_reward"],
                    room["enemy"]["is_alive"]
                ) if room["enemy"] else None,
                room["lootable_coins"],
                StrengthPotion() if room["lootable_potions"] else None,
                room["intro_played"]
            ) for room in room_save_data
        ]
        self.current_room = self.rooms[current_room_index_save_data]

    def start(self):
        if self.intro_played is False:
            with open(f"dialogues/intro.json", "r") as file:
                data = json.load(file)
                for text in data["intro_texts"]:
                    clear_console()
                    print(text)
                    input("Press enter to continue...")
            self.intro_played = True

        self.menu()

    def menu(self):
        clear_console()
        print(f"Hello {self.player.name}")
        print(f"You are currently in {self.current_room.name}")

        print(f"Equipped weapon: {self.player.equipped_weapon.name if self.player.equipped_weapon else 'No weapon equipped'}")
        print(f"Effects: {'Strength' if self.player.has_strength_effect else 'No effect'}")

        print("What would you like to do?")
        print("1. Travel")
        print("2. Loot the room")
        print("3. Inventory")
        print("4. Save and Quit")

        selection = input()

        match selection:
            case "1":
                self.travel_menu(self.menu)
            case "2":
                self.current_room.loot(self.player.inventory, self.menu)
            case "3":
                self.player.inventory.print(self.player, self.menu)
            case "4":
                self.save_system.save(self)
                print()
            case _:
                clear_console()
                print("Invalid selection")
                input("Press enter to continue...")
                self.menu()

    def travel_menu(self, main_menu):
        clear_console()

        choice_amount = 0

        print("Where would you like to travel?")
        for floor_index in range(1, self.highest_unlocked_floor + 1):
            print(f"Floor {floor_index}")
            for room_index, room in enumerate(self.rooms):
                if room.floor == floor_index:
                    choice_amount += 1
                    print(f"{room_index + 1}. {room.name}")

        selection = input()

        try:
            int(selection)
        except:
            clear_console()
            print("Invalid room selection")
            input("Press enter to continue...")
            return main_menu()

        if 1 <= int(selection) <= choice_amount:
            if self.rooms[int(selection) - 1].travel_successful(self.player):
                self.current_room = self.rooms[int(selection) - 1]
                if self.is_floor_cleared(self.highest_unlocked_floor):
                    if self.highest_unlocked_floor == 3:
                        print("You won the game!")
                        return
                    clear_console()
                    self.highest_unlocked_floor += 1
                    print(f"You have unlocked floor {self.highest_unlocked_floor}")
                    input("Press space to continue...")
            return main_menu()
        else:
            clear_console()
            print("Invalid room selection")
            input("Press enter to continue...")
            return main_menu()

    def is_floor_cleared(self, floor):
        for room in self.rooms:
            if room.floor == floor and room.enemy:
                if room.enemy.is_alive:
                    return False
        return True

