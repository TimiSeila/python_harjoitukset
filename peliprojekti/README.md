## Destory the CO2 Monsters

# Timi Seila

```text
Game structure
├── main.py
└── modules
    ├── player.py
    |   ├── class Player
    |   |   ├── name 
    |   |   ├── age
    |   |   ├── max_health
    |   |   ├── current_health
    |   |   ├── inventory 
    |   |   ├── equipped_weapon
    |   |   ├── has_strength_effect
    |   |   └── replenish_health()
    |   └── class Inventory 
    |       ├── coins
    |       ├── owned_weapons 
    |       ├── owned_potions
    |       ├── print()
    |       ├── add_coins()
    |       ├── add_weapon()
    |       ├── add_potion()
    |       ├── equip_weapon()
    |       └── consume_potion() 
    ├── enemy.py
    |   └── class Enemy
    |       ├── name 
    |       ├── max_health
    |       ├── health
    |       ├── attack_power 
    |       ├── coin_reward
    |       └── is_alive 
    ├── game.py
    |   └── class Game
    |       ├── save_system
    |       ├── player
    |       ├── shop
    |       ├── intro_played
    |       ├── highest_floor_unlocked
    |       ├── rooms
    |       ├── current_room
    |       ├── start()
    |       ├── end()
    |       ├── menu()
    |       ├── travel_menu()
    |       └── is_floor_cleared()
    ├── shop.py
    |   └── class Shop
    |       ├── available_weapons
    |       ├── available_potions
    |       ├── print()
    |       ├── print_weapons()
    |       ├── print_potions()
    |       ├── buy_weapon()
    |       └── buy_potion()
    ├── save.py
    |   └── class SaveSystem
    |       ├── has_save_file()
    |       ├── save()
    |       ├── load_player()
    |       ├── load_inventory()
    |       ├── load_shop()
    |       ├── load_intro_played()
    |       ├── load_highest_unlocked_floor()
    |       ├── load_rooms()
    |       └── load_current_room_index()
    ├── weapon.py
    |   └── class Weapon
    |       ├── name
    |       ├── damage 
    |       └── cost
    ├── room.py
    |   └── class Room
    |       ├── name
    |       ├── floor
    |       ├── enemy
    |       ├── lootable_coins
    |       ├── lootable_potion
    |       ├── intro_played
    |       ├── travel_successful()
    |       ├── battle_loop()
    |       └── loot()
    ├── helpers.py
    |   ├── enter_break()
    |   ├── invalid_selection()
    |   └── clear_console()
    └── potion.py
        └── class StrengthPotion 
            ├── name
            ├── cost
            └── strength
```
