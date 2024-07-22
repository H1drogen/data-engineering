from src.pokemon import Pokemon

class Battle():
    def __init__(self, pokemon_1, pokemon_2):
        self.pokemon_1 = pokemon_1
        self.pokemon_2 = pokemon_2
        self.player_turn = 1

    def take_turn(self):
        if self.player_turn == 1:
            attacker = self.pokemon_1
            defender = self.pokemon_2
            self.player_turn = 2
        else:
            attacker = self.pokemon_2
            defender = self.pokemon_1
            self.player_turn = 1
        damage = attacker.pokemon.attack_damage * attacker.get_multiplier(defender)
        defender.pokemon.take_damage(damage)
        if defender.pokemon.has_fainted():
            raise Exception(f'{defender.pokemon.name} has fainted')

    def get_winner(self):
        if self.pokemon_2.pokemon.has_fainted():
            return self.pokemon_1
        if self.pokemon_1.pokemon.has_fainted():
            return self.pokemon_2
        return None












    