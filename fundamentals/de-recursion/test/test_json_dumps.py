from src.json import dumps

def test_json_dumps_returns_string_with_empty_dictionary():
    assert isinstance(dumps({}), str)

def test_json_dumps_returns_json_with_single_key_value_pair():
    assert dumps({1: "welcome"}) == '{"1": "welcome"}'

def test_json_dumps_returns_json_with_multiple_key_value_pairs():
    input = {1: "welcome", 2: "to", 3: "python"}
    expected_json_output = '{"1": "welcome", "2": "to", "3": "python"}'
    assert dumps(input) == expected_json_output

def test_json_dumps_removes_tuples():
    Dictionary = {(1, 2, 3): 'Welcome', 2: 'to',
                  3: 'Geeks', 4: 'for',
                  5: 'Geeks'}
    expected_output = '{"2": "to", "3": "Geeks", "4": "for", "5": "Geeks"}'
    assert dumps(Dictionary) == expected_output