from modules.player import Player
from modules.room import Room
from modules.weapon import Weapon
from modules.helpers import clear_console

class Game:
    def __init__(self):
        self.player = Player("Player", 100)
        self.current_room = Room("Garbage room")

    def menu(self):
        clear_console()
        print("What would you like to do?")
        print("1. Travel")
        print("2. Inventory")
        print("3. Save and Quit")

        selection = input()

        match selection:
            case "1":
                self.travel([self.current_room])
            case "2":
                # TODO check inventory
                self.player.inventory.print()
                print()
            case "3":
                # TODO save and quit
                print()
            case _:
                print("Invalid selection")

    def travel(self, available_rooms):
        clear_console()
        print("Where would you like to travel?")
        for index, room in enumerate(available_rooms):
            print(f"{index + 1}. {room.name}")
