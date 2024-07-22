import pytest
from src.iterators.enumerator import NCEnumerate


def test_enumerator_has_attributes_list_and_index():
    test_list = [1,2,3,4]
    e = NCEnumerate(test_list)
    assert hasattr(e, 'list')
    assert hasattr(e, 'index')

def test_enumerator_returns_itself_when_iterated():
    test_list = [1,2,3,4]
    e = NCEnumerate(test_list)
    assert iter(e) == e






def test_enumerator_takes_list_and_returns_appropriate_next_item():
    test_list = [1,2,3,4]
    e = NCEnumerate(test_list)
    assert next(e) == (0,1)
    assert next(e) == (1,2)

def test_enumerator_works_as_iterator():
    assertion = []
    test_list = [1,2,3,4]
    e = NCEnumerate(test_list)
    for number in e:
        assertion.append(number)
    assert assertion == [(0,1),(1,2),(2,3),(3,4)]



def test_enumerator_is_an_iterator():
    # implement me
    pass

def test_StopIteration_exception_is_raised_at_the_end_of_iteration():
    test_list = [1,2]
    e = NCEnumerate(test_list)
    next(e)
    next(e)
    with pytest.raises(StopIteration):
        next(e)
