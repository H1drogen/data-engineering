from src.Divisions import calculate_divisors


def test_divisions_works_with_0():
    assert calculate_divisors(0) == 0

def test_divisions_works_with_1():
    assert calculate_divisors(1) == 0

def test_disions_works_with_10():
    assert calculate_divisors(10) == 23
