from src.pokeball import Pokeball

class Trainer(Pokeball):
    def __init__(self):
        pokeball_1 = Pokeball()
        pokeball_2 = Pokeball()
        pokeball_3 = Pokeball()
        pokeball_4 = Pokeball()
        pokeball_5 = Pokeball()
        pokeball_6 = Pokeball()
        self.belt = (
            pokeball_1, 
            pokeball_2, 
            pokeball_3, 
            pokeball_4,
            pokeball_5,
            pokeball_6
        )

    def throw_pokeball(self, Pokemon):
        if self.belt[5].is_empty == False:
            raise Exception('Belt is full')
        for num in range(0, 5):
            if self.belt[num].is_empty() == True:
                self.belt[num].catch(Pokemon)
        pass