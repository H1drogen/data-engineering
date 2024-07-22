from src.alternate_case import alternate_case



def test_alternate_case_returns_string():
    word = 'Hello'
    answer = alternate_case(word)

    assert type(answer) is str

def test_alternate_case_starts_with_capital():
    word = 'hello'
    answer = alternate_case(word)

    assert answer[0].isupper()

def test_alternate_case_returns_alternate_with_one_word():
    word = 'hello'
    answer = alternate_case(word)
    expected = 'HeLlO'

    assert answer == expected

