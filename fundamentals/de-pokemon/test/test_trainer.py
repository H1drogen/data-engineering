from src.trainer import Trainer
from src.pokemon import Pokemon
def test_trainer_has_6_pokeballs_when_initialised():
    
    trainer = Trainer()
    test_belt = trainer.belt
    assert len(test_belt) == 6

def test_throw_first_pokeball_catches_pokemon():
    trainer = Trainer()
    test_pokemon = Pokemon('Pikachu', 150, 75, 'thunderbolt')
    test_throw = trainer.throw_pokeball(test_pokemon)
   
    assert trainer.belt[0].is_empty() == False

def test_second_pokeball_catches_pokemon():
    trainer = Trainer()
    test_pokemon = Pokemon('Pikachu', 150, 75, 'thunderbolt')
    trainer.throw_pokeball(test_pokemon)
    trainer.throw_pokeball(test_pokemon)
    
    assert trainer.belt[1].is_empty() == False

