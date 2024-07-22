from src.count_punctuation import count_punctuation


def test_count_punctuation_returns_0_with_empty_string():
    assert count_punctuation("") == 0

def test_count_punctuation_returns_1_with_single_punctuation():
    assert count_punctuation("!") == 1

def test_count_punctuation_returns_5_with_multiple_punctuation():
    assert count_punctuation("Ready? Set... Go!") == 5
