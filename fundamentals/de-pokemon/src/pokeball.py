from src.pokemon import Pokemon

class Pokeball(Pokemon):
    def __init__(self, Pokemon = None):
        self.pokemon = Pokemon

    def catch(self, Pokemon):
        if self.pokemon == None:
            self.pokemon = Pokemon
        else:
            raise Exception(f'Pokeball already contains {self.pokemon.name}')

    def is_empty(self):
        if self.pokemon == None:
            return True
        return False