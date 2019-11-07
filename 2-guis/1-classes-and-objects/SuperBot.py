from Bot import Bot

class Superbot(Bot):
    def __init__(self, name, age, energy, shield_level, super_power_level =0):
        super().__init__(name, age, energy, shield_level)
        self.super_power_level = super_power_level
        print()

    def display_super_power_level(self):
        print("Super Power level: " + str(self.super_power_level))
        print()