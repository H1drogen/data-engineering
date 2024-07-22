from src.pokeball import Pokeball
from src.pokemon import Pokemon

def test_pokeball_has_no_pokemon_when_initialised():
    initial = Pokeball()
    assert initial.pokemon == None

def test_catch_stores_passed_pokemon():
    test_pokeball = Pokeball()
    test_pokemon = Pokemon('Pikachu', 150, 75, 'thunderbolt')
    test_pokeball.catch(test_pokemon)

    assert  test_pokeball.pokemon == test_pokemon

def test_is_empty_returns_correct_boolean():
    
    test_is_empty = Pokeball().is_empty()
    assert test_is_empty == True