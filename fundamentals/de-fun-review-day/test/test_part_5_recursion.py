# Your tests here
from src.part_5_recursion import flatten, deep_entries


def test_flatten_works_on_regular_list():
    assert flatten([1,2,3]) == [1,2,3]

def test_flatten_works_on_single_nested_list():
    assert flatten([1, 2, [3, 4]]) == [1,2,3,4]

def test_flatten_implicitely_flatens_to_one_level_on_double_nested_list():
    assert flatten([1, 2, [3, [4, [5, 6]]]]) == [1, 2, 3, [4, [5, 6]]]

def test_flatten_fully_flatens_list_when_depth_specified():
    assert flatten([1, [2], [3, [4, [5, 6]]]], 25) == [1, 2, 3, 4, 5, 6]

def test_deep_entries_returns_tuple():
    assert isinstance(deep_entries({}), tuple)

def test_deep_entries_converts_simple_dictionary_into_tuple():
    input = {'name': 'Sam'}
    expected = (('name', 'Sam'),)
    assert deep_entries(input) == expected

def test_deep_entries_converts_multiple_key_dictionary_into_tuple():
    input = {'name': 'Sam', 'fave_book': '50 Shades of Python'}
    expected = (('name', 'Sam'), ('fave_book', '50 Shades of Python'))
    assert deep_entries(input) == expected

def test_deep_entries_converts_nested_dictionary_into_tuple():
    input = {'name': 'Sam', 'pets': {'name': 'fido'}}
    expected = (('name', 'Sam'), ('pets',(('name', 'fido'),)))
    assert deep_entries(input) == expected

def test_deep_entries_converts_even_more_nested_dictionary_into_tuple():
    input = {
        'name': 'Sam',
        'pets': {'name': 'Fido'},
        'fave_book': { 'title': '50 Shades of Python', 'author': { 'first_name': 'Cody', 'last_name': 'Smutt' }}
    }
    expected = (
        ('name', 'Sam'),
        ('pets', (('name', 'Fido'),)),
        ('fave_book', (('title', '50 Shades of Python'), ('author', (('first_name', 'Cody'), ('last_name', 'Smutt')))))
    )
    assert deep_entries(input) == expected
