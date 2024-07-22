from src.deep_includes import deep_includes


def test_deep_includes_returns_true_with_single_list():
    assert deep_includes([1, 2, 3], 2) == True

def test_deep_includes_returns_true_with_nested_list():
    assert deep_includes([1, 2, [3, 4]], 4) == True