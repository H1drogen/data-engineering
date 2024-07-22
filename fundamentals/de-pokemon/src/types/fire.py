from src.pokemon import Pokemon


class Fire(Pokemon):
    def __init__(self, Pokemon):
        self.type = 'fire'
        self.strong_against = ['grass']
        self.weak_against = ['water']
        self.pokemon = Pokemon

    def get_multiplier(self, pokemon_type):
        
        if pokemon_type.type in self.strong_against:
            return 1.5
        if pokemon_type.type in self.weak_against:
            return 0.5
        else:
            return 1