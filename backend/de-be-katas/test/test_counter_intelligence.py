from src.counter_intelligence import counter_intelligence


def test_encrypted_str_returns_X_as_last_character():
    encrypted_str = "X"
    assert counter_intelligence(encrypted_str) == "X"

def test_encrypted_str_is_able_decript_encrypted_character():
    encrypted_str = "Y"
    assert counter_intelligence(encrypted_str) == "X"

def test_encrypted_str_always_returns_X_as_last_character_with_encrypted_string():
    encrypted_str = 'BCD Y'
    assert counter_intelligence(encrypted_str)[-1] == 'X'

def test_encrypte_str_returns_decrypted_string():
    encrypted_str = "BCDY"
    assert counter_intelligence(encrypted_str) == "ABCX"

def test_encrypted_str_returns_decrypted_string_with_spaces_and_special_characters():
    encrypted_str = "ngbk g toik jge :) d"
    assert counter_intelligence(encrypted_str) == "HAVE A NICE DAY :) X"


