from src.iterators.map import NCMap

def test_map_has_attributes_list_and_function():
    test_list = [1,2,3,4]
    def multiply10(a):
        return a * 10
    e = NCMap(multiply10, test_list)
    assert hasattr(e, 'list')
    assert hasattr(e, 'function')

def test_map_returns_itself_when_iterated():
    test_list = [1,2,3,4]
    def multiply10(a):
        return a * 10
    e = NCMap(multiply10, test_list)
    assert iter(e) == e



def test_map_iterates_through_whole_list():
    test_list = [1,2,3,4]
    count = 0
    def multiply10(a):
        return a * 10
    e = NCMap(multiply10, test_list)
    for value in e:
        count += 1
    assert count == 4

def test_map_applies_transformation():
    test_list = [1,2,3,4]
    def multiply10(a):
        return a * 10
    e = NCMap(multiply10, test_list)
    assert next(e) == 10

def test_map_applies_transformation_to_whole_list():
    test_list = [1,2,3,4]
    count = 0
    def multiply10(a):
        return a * 10
    e = NCMap(multiply10, test_list)
    next(e)
    next(e)
    next(e)
    next(e)
    # assert none