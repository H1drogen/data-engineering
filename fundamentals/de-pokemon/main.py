from src.battle import Battle
from src.pokemon import Pokemon
from src.trainer import Trainer
from src.types.electric import Electric
from src.types.fire import Fire
from src.types.grass import Grass
from src.types.normal import Normal
from src.types.water import Water


def main():
    trainer1 = Trainer()
    trainer2 = Trainer()

    print('Hello, Please pick pokemon from list below \n')
    p1 = Electric(Pokemon('Pikachu', 100, 10, 'thunderbolt'))
    p2 = Fire(Pokemon('Charmander', 44, 17, 'flamethrower'))
    p3 = Grass(Pokemon('Bulbasaur', 45, 16, 'razor leaf'))
    p4 = Water(Pokemon('Squirtle', 44, 16, 'surf'))
    p5 = Normal(Pokemon('Eevee', 55, 18, 'headbutt'))
    p6 = Water(Pokemon('Vaporeon', 70, 19, 'hydro pump'))
    p7 = Grass(Pokemon('Leafeon', 65, 17, 'giga drain'))
    p8 = Fire(Pokemon('Flareon', 65, 20, 'fire blast'))

    available_pokemon = [p1, p2, p3, p4, p5, p6, p7, p8]
    for pokemon in available_pokemon:
        print(f'{pokemon.pokemon.name}')

    choice = input("\nPlease type choice here: ")
    p1 = add_pokemon(trainer1, choice, available_pokemon)

    opponent = input('\nPick your opponent: ')
    p2 = add_pokemon(trainer2, opponent, available_pokemon)

    try:
        active_pokemon1 = trainer1.belt[0].pokemon
        active_pokemon2 = trainer2.belt[0].pokemon
        battle = Battle(active_pokemon1, active_pokemon2)
        while not (active_pokemon1.has_fainted() or active_pokemon2.has_fainted()):
            battle.take_turn()
            print(f'{active_pokemon1.name} has {active_pokemon1.hit_points} hp left and {active_pokemon2.name} has {active_pokemon2.hit_points} left')
            input('continue to next turn?')
    except:
        print(f'{battle.get_winner()} wins!')




def add_pokemon(trainer, pokemon, available_pokemon):
    for p in available_pokemon:
        if p.pokemon.name == pokemon:
            print(f'{p.pokemon.name} is caught!')
            trainer.throw_pokeball(p.pokemon)
            return p
    raise Exception('Pokemon not available')



if __name__ == "__main__":
    main()