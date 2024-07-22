from src.sum_int import sum_int


def test_sum_int_returns_integer():
    assert isinstance(sum_int(2), int)

def test_sum_int_works_with_1():
    assert sum_int(1) == 1

def test_sum_int_works_with_4():
    assert sum_int(4) == 10