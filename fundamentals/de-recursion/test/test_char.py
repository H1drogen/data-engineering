from src.contains_char import contains_char


def test_contains_char_takes_two_arguments_and_returns_boolean():
    assert isinstance(contains_char("f","f"), bool)

def test_contains_char_returns_same_character_true():
    assert contains_char("f","f") == True

def test_contains_char_returns_True_for_y_in_eggy_bread():
    assert contains_char("eggy bread", "y") == True