## Destory the CO2 Monsters

# Timi Seila

```text
Game structure
├── main.py
└── modules
    ├── player.py
    |   ├── class Player
    |   |   ├── name 
    |   |   ├── max_health
    |   |   ├── health
    |   |   ├── inventory 
    |   |   ├── equipped_weapon
    |   |   ├── has_strength_effect
    |   |   └── has_vitality_effect 
    |   └── class Inventory 
    |       ├── coins
    |       ├── owned_weapons 
    |       ├── owned_potions
    |       ├── print()
    |       ├── add_coins()
    |       ├── add_weapon()
    |       └── add_potion() 
    ├── enemy.py
    |   └── class Enemy
    |       ├── name 
    |       ├── max_health
    |       ├── health
    |       ├── attack_power 
    |       ├── c02_emissions
    |       └── coin_reward 
    ├── game.py
    |   └── class Game
    |       ├── player
    |       ├── menu()
    |       └── travel()
    ├── quest.py
    |   ├── class Quest
    |   |   └── name
    |   └── class QuestSystem
    |       └── quest_queue 
    ├── weapon.py
    |   └── class Weapon
    |       ├── name
    |       ├── damage 
    |       └── cost
    ├── room.py
    |   └── class Room
    |       └── name
    ├── helpers.py
    |   └── clear_console()
    └── potion.py
        └── class Potion 
            ├── name
            ├── cost
            ├── subclass StrengthPotion
            |   └── strength 
            └── subclass VitalityPotion
                └── vitality
```
