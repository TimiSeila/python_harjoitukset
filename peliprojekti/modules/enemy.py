class Enemy:
    def __init__(self, name, max_health, attack_power, coin_reward, is_alive):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.attack_power = attack_power
        self.coin_reward = coin_reward
        self.is_alive = is_alive
