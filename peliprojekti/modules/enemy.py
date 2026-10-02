class Enemy:
    def __init__(self, name, max_health, attack_power, co2_emissions, coin_reward):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.attack_power = attack_power
        self.co2_emissions = co2_emissions
        self.coin_reward = coin_reward
