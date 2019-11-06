from SuperBot import SuperBot

class FlyingBot(SuperBot):
    def __init__(self, name, age, energy, shield_level, hover_distance =0):
        super().__init__(name, age, energy, shield_level)
        self.hover_distance = hover_distance
        
    def display_hover_distance(self):
        print(self.hover_distance)

