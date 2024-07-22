from src.pokemon import Pokemon


class Electric(Pokemon):
    def __init__(self, Pokemon):
        self.type = 'electric'
        self.strong_against = ['water']
        self.weak_against = []
        self.pokemon = Pokemon 
    
    def get_multiplier(self, pokemon):
        
        if pokemon.type in self.strong_against:
            return 1.5
        if pokemon.type in self.weak_against:
            return 0.5
        else:
            return 1

