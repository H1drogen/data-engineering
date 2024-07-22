from src.sum_digits import sum_digits


def test_sum_digits_returns_digit_with_single_digit():
    assert sum_digits(3) == 3

def test_sum_digits_returns_sum_of_digits_with_multiple_digits():
    assert sum_digits(123) == 6
