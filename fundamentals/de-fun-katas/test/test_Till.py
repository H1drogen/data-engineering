from src.Till import till_addition


def test_till_works_with_empty_dict():
    assert till_addition({}) == '£0.0'

def test_till_with_single_denomination():
    till = {
        '1p': 1
    }
    assert till_addition(till) == '£0.01'

def test_till_works_with_many_denominations():
    till = {
        '1p': 100,
        '2p': 50,
        '5p': 20,
        '10p': 10,
        '20p': 5,
        '50p': 2,
        '£1': 1,
        '£2': 0,
        '£5': 0,
        '£10': 0,
        '£20': 0,
        '£50': 0
    }
    assert till_addition(till) == '£7.0'