from src.types.electric  import Electric
from src.types.water  import Water
from src.types.normal  import Normal
from src.types.fire import Fire
from src.pokemon import Pokemon

def test_get_multiplier_returns_correct_multiplier_if_strong_against():
        
    lvl_50_pikachu = Pokemon('Pikachu', 150, 75, 'thunderbolt')
    lvl_50_vaporeon = Pokemon('Vaporeon', 70, 19, 'hydro pump')
    test_function = Electric(lvl_50_pikachu)
    test_function2 = Water(lvl_50_vaporeon)
    get_multiplier = test_function.get_multiplier(test_function2)
    assert get_multiplier == 1.5

def test_get_multiplier_returns_correct_multiplier():
        
    lvl_50_eevee = Pokemon('Eevee', 55, 18, 'headbutt')
    lvl_50_flareon = Pokemon('Flareon', 65, 20, 'Fire blast')
    test_function = Normal(lvl_50_eevee)
    test_function2 = Fire(lvl_50_flareon)
    get_multiplier = test_function.get_multiplier(test_function2)
    assert get_multiplier == 1

def test_get_multiplier_returns_correct_multiplier_if_weak_against():
        
    lvl_50_vaporeon = Pokemon('Vaporeon', 70, 19, 'hydro pump')
    lvl_50_flareon = Pokemon('Flareon', 65, 20, 'Fire blast')
    test_function = Fire(lvl_50_flareon)
    test_function2 = Water(lvl_50_vaporeon)
    get_multiplier = test_function.get_multiplier(test_function2)
    assert get_multiplier == 0.5