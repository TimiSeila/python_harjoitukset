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
    |   |   └── equipped_weapon 
    |   └── class Inventory 
    |       ├── coins
    |       ├── owned_weapons 
    |       └── owned_potions 
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
    |       └── player
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
    └── potion.py
        └── class Potion 
            ├── name
            ├── cost
            ├── subclass StrengthPotion
            |   └── strength 
            └── subclass VitalityPotion
                └── vitality
```
