from src.deep_total import deep_total


def test_deep_total_without_nested_lists():
    assert (deep_total([1, 2, 3]) == 6)

def test_deep_total_with_nested_lists():
    assert (deep_total([1, [2, 3], 4]) == 10)

def test_deep_total_with_deeply_nested_lists():
    assert (deep_total([1, [2, [3, 4], 5], 6]) == 21)