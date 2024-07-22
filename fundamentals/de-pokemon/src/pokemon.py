
class Pokemon():
    def __init__(self, pokemon_name, hit_points, attack_damage, move):
        self.name = pokemon_name
        self.hit_points = hit_points
        self.attack_damage = attack_damage
        self.move = move
        
    def use_move(self):
        return f"{self.name} used {self.name}'s {self.move}"
        # "PokemonX used PokemonX's move"

    def take_damage(self, damage):
        self.hit_points -= damage

    def has_fainted(self):
        if self.hit_points <= 0:
            return True
        return False





