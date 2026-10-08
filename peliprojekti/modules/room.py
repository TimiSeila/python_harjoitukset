import json
import time
from modules.helpers import clear_console, enter_break

class Room():
    def __init__(self, name, floor, enemy, lootable_coins, lootable_potion, intro_played):
        self.name = name
        self.floor = floor
        self.enemy = enemy
        self.lootable_coins = lootable_coins
        self.lootable_potion = lootable_potion
        self.intro_played = intro_played

        with open("dialogues/rooms.json", "r") as file:
            data = json.load(file)

        self.room_dialogue_data = data[self.name]

    def travel_successful(self, player):
        clear_console()
        if self.intro_played is False:
            print(self.room_dialogue_data["intro"])
            enter_break()
        if self.enemy and self.enemy.is_alive is True:
            return self.battle_loop(player)
        else:
            self.intro_played = True
            return True

    def battle_loop(self, player):
        clear_console()
        print(f"You are facing {self.enemy.name}")
        player_damage_boost = 30 if player.has_strength_effect else 0

        print("Your stats:")
        print(f"Health: {player.current_health}")
        print(f"Attack Power: {player.equipped_weapon.damage + player_damage_boost}")

        print("Enemy stats:")
        print(f"Health: {self.enemy.max_health}")
        print(f"Attack Power: {self.enemy.attack_power}")

        enter_break()

        clear_console()
        self.enemy.current_health = self.enemy.max_health
        while True:
            time.sleep(1)
            clear_console()
            self.enemy.current_health -= player.equipped_weapon.damage + player_damage_boost
            print(f"You deal {player.equipped_weapon.damage + player_damage_boost} damage to {self.enemy.name}")

            print(f"Your health: {player.current_health if player.current_health > 0 else 0}")
            print(f"Enemy health: {self.enemy.current_health if self.enemy.current_health > 0 else 0}")

            if self.enemy.current_health <= 0:
                print(self.room_dialogue_data["victory"])
                print(f"{self.enemy.name} has been defeated!")
                self.enemy.is_alive = False
                self.intro_played = True
                player.has_strength_effect = False
                player.replenish_health()
                player.inventory.add_coins(self.enemy.coin_reward)
                enter_break()
                return True

            player.current_health -= self.enemy.attack_power
            print(f"{self.enemy.name} deals {self.enemy.attack_power} damage to you")

            print(f"Your health: {player.current_health if player.current_health > 0 else 0}")
            print(f"Enemy health: {self.enemy.current_health if self.enemy.current_health > 0 else 0}")

            if player.current_health <= 0:
                print(self.room_dialogue_data["loss"])
                print(f"You have been defeated by {self.enemy.name}")
                player.has_strength_effect = False
                player.replenish_health()
                enter_break()
                return False

        self.enemy.is_alive = False


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

        enter_break()
        main_menu()

