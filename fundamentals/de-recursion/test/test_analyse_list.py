from src.analyse_list import analyse_list


def test_analyse_list_returns_indexed_dictionary_with_single_list():
    input_list = ["carrot", "car", "boat"]
    expected_output = {
        'mabel.0': 'carrot',
        'mabel.1': 'car',
        'mabel.2': 'boat'
    }
    assert analyse_list("mabel", input_list) == expected_output


def test_analyse_list_returns_true_with_nested_list():
    nested_list = ["carrot", ["car", "boat", "plane"], "turtle", ["house"]]
    expected_output = {
        "mabel.0": "carrot",
        "mabel.1.0": "car",
        "mabel.1.1": "boat",
        "mabel.1.2": "plane",
        "mabel.2": "turtle",
        "mabel.3.0": "house"
    }
    assert analyse_list("mabel", nested_list) == expected_output
