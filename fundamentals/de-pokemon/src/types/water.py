from src.pokemon import Pokemon


class Water(Pokemon):
    def __init__(self, Pokemon):
        self.type = 'water'
        self.strong_against = ['fire']
        self.weak_against = ['grass', 'electric']
        self.pokemon = Pokemon
    
    def get_multiplier(self, pokemon):
        
        if pokemon.type in self.strong_against:
            return 1.5
        if pokemon.type in self.weak_against:
            return 0.5
        else:
            return 1
