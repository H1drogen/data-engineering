from src.pokemon import Pokemon


def test_pokemon_instantiates_with_appropriate_parameters():
    name = 'Pikachu'
    hp = 150
    damage = 75
    move = 'thunderbolt'
    lvl50_pikachu = Pokemon(name, hp, damage, move)
    assert lvl50_pikachu is not None

def test_pokemon_use_move_returns_correct_string():
    name = 'Pikachu'
    hp = 150
    damage = 75
    move = 'thunderbolt'
    test_class = Pokemon(name, hp, damage, move)
    move_executed = test_class.use_move()
    assert move_executed == "Pikachu used Pikachu's thunderbolt"

def test_pokemon_take_damage_reduces_health_by_move_damage():
    name = 'Pikachu'
    hp = 150
    damage = 75
    move = 'thunderbolt'
    lvl_50_pikachu = Pokemon(name, hp, damage, move)
    lvl_50_pikachu.take_damage(50)
    assert lvl_50_pikachu.hit_points == 100

def test_pokemon_has_fainted_returns_True_when_health_reaches_0():
    name = 'Pikachu'
    hp = 150
    damage = 75
    move = 'thunderbolt'
    lvl_50_pikachu = Pokemon(name, hp, damage, move)
    assert lvl_50_pikachu.has_fainted() == False
    lvl_50_pikachu.take_damage(150)
    assert lvl_50_pikachu.has_fainted() == True
    lvl_50_pikachu.take_damage(30)
    assert lvl_50_pikachu.has_fainted() == True


