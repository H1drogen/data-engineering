from src.sum_ascii import sum_ascii


def test_returns_ascii_for_single_name():
    word = ['John']
    answer = sum_ascii(word)

    assert answer == 'John'

def test_returns_ascii_for_list_of_names():
    List = ['John', 'ooo', 'hhh', 'nnnn']
    answer = sum_ascii(List)

    assert answer == 'nnnn'
