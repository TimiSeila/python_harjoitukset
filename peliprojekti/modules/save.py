import json
import os

class SaveSystem:
    def has_save_file(self):
        save_file = "save/save.json"
        if os.path.isfile(save_file):
            return True
        else:
            return False

    def save(self, game):
        player = game.player
        inventory = player.inventory
        data = {
            "player": {
                "name": player.name,
                "max_health": player.max_health,
                "current_health": player.current_health,
                "equipped_weapon": {
                    "name": player.equipped_weapon.name,
                    "damage": player.equipped_weapon.damage,
                    "cost": player.equipped_weapon.cost
                },
                "has_strength_effect": player.has_strength_effect
            },
            "inventory": {
                "coins": inventory.coins,
                "owned_weapons": [
                    {
                        "name": weapon.name,
                        "damage": weapon.damage,
                        "cost": weapon.cost
                    } for weapon in game.player.inventory.owned_weapons
                ],
                "owned_potions": [
                    {
                        "name": potion.name,
                        "cost": potion.cost,
                        "strength": potion.strength
                    } for potion in game.player.inventory.owned_potions
                ]
            },
            "shop": {
                "available_weapons": [{
                    "name": weapon.name,
                    "damage": weapon.damage,
                    "cost": weapon.cost
                } for weapon in game.shop.available_weapons] 
            },
            "intro_played": game.intro_played,
            "highest_unlocked_floor": game.highest_unlocked_floor,
            "rooms": [{
                "name": room.name,
                "floor": room.floor,
                "enemy": {
                    "name": room.enemy.name,
                    "max_health": room.enemy.max_health,
                    "attack_power": room.enemy.attack_power,
                    "co2_emissions": room.enemy.co2_emissions,
                    "coin_reward": room.enemy.coin_reward,
                    "is_alive": room.enemy.is_alive
                } if room.enemy else "",
                "lootable_coins": room.lootable_coins,
                "lootable_potions": room.lootable_potion,
                "intro_played": room.intro_played
            } for room in game.rooms],
            "current_room_index": game.rooms.index(game.current_room)
        }

        with open("save/save.json", "w") as file:
            json.dump(data, file)

    def load_player(self, save_file_path):
        with open(f"save/{save_file_path}", "r") as file:
            data = json.load(file)
            return data["player"]

    def load_inventory(self, save_file_path):
        with open(f"save/{save_file_path}", "r") as file:
            data = json.load(file)
            return data["inventory"]

    def load_shop(self, save_file_path):
        with open(f"save/{save_file_path}", "r") as file:
            data = json.load(file)
            return data["shop"]

    def load_intro_played(self, save_file_path):
        with open(f"save/{save_file_path}", "r") as file:
            data = json.load(file)
            return data["intro_played"]

    def load_highest_unlocked_floor(self, save_file_path):
        with open(f"save/{save_file_path}", "r") as file:
            data = json.load(file)
            return data["highest_unlocked_floor"]

    def load_rooms(self, save_file_path):
        with open(f"save/{save_file_path}", "r") as file:
            data = json.load(file)
            return data["rooms"]

    def load_current_room_index(self, save_file_path):
        with open(f"save/{save_file_path}", "r") as file:
            data = json.load(file)
            return data["current_room_index"]
