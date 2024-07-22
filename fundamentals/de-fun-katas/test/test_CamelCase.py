from src.CamelCase import sentence_to_camel_case

def test_camel_case_works_with_single_word():
    assert sentence_to_camel_case('this', True) == 'This'

def test_camel_case_works_with_multiple_words():
    assert sentence_to_camel_case('this sentence', True) == 'ThisSentence'

def test_camel_case_works_with_bigger_sentence():
    assert sentence_to_camel_case('this is a bigger sentence', True) == 'ThisIsABiggerSentence'

def test_camel_case_works_with_single_word_false():
    assert sentence_to_camel_case('Hello', False) == 'hello'

def test_camel_case_works_with_multiple_words_false():
    assert sentence_to_camel_case('this sentence', False) == 'thisSentence'