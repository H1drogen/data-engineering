from src.battle import Battle
from src.pokemon import Pokemon
from src.types.electric import Electric
from src.types.fire import Fire
from src.types.normal import Normal

import pytest

from src.types.water import Water


def test_battle_class_has_2_pokemon():
    lvl_50_pikachu = Pokemon('Pikachu', 150, 75, 'thunderbolt')
    lvl_50_vaporeon = Pokemon('Vaporeon', 70, 19, 'hydro pump')
    test_battle = Battle(lvl_50_pikachu, lvl_50_vaporeon)
    assert test_battle.pokemon_1 == lvl_50_pikachu
    assert test_battle.pokemon_2 == lvl_50_vaporeon

def test_take_turn_inflicts_damage_on_p2():
    lvl_50_eevee = Normal(Pokemon('Eevee', 55, 18, 'headbutt'))
    lvl_50_flareon = Fire(Pokemon('Flareon', 65, 20, 'Fire blast'))

    test_battle = Battle(lvl_50_eevee, lvl_50_flareon)
    test_battle.take_turn()
    assert test_battle.pokemon_2.pokemon.hit_points == (65 - 18)

def test_take_turn_switches_over_on_p1():
    lvl_50_eevee = Normal(Pokemon('Eevee', 55, 18, 'headbutt'))
    lvl_50_flareon = Fire(Pokemon('Flareon', 65, 20, 'Fire blast'))

    test_battle = Battle(lvl_50_eevee, lvl_50_flareon)
    test_battle.take_turn()
    test_battle.take_turn()

    assert test_battle.pokemon_1.pokemon.hit_points == (55 - 20)

def test_take_turn_causes_pokemon_to_faint():
    lvl_50_pikachu = Electric(Pokemon('Pikachu', 150, 75, 'thunderbolt'))
    lvl_50_vaporeon = Water(Pokemon('Vaporeon', 70, 19, 'hydro pump'))

    test_battle = Battle(lvl_50_pikachu, lvl_50_vaporeon)

    with pytest.raises(Exception, match = 'Vaporeon has fainted'):
        test_battle.take_turn()

def test_get_winner_returns_appropriate_winner_of_battle():
    try:
        lvl_50_pikachu = Electric(Pokemon('Pikachu', 150, 75, 'thunderbolt'))
        lvl_50_vaporeon = Water(Pokemon('Vaporeon', 70, 19, 'hydro pump'))

        test_battle = Battle(lvl_50_pikachu, lvl_50_vaporeon)
        test_battle.take_turn()
    except:
        assert test_battle.get_winner() == lvl_50_pikachu
