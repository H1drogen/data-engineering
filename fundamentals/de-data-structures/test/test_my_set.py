from src.my_set import set

def test_my_set_instantiates_with_empty_storage():
    new_set = set()
    assert new_set.storage == []

def test_add_method_adds_element_to_storage():
    new_set = set()
    new_set.add('item')
    assert new_set.storage == ['item']

def test_add_method_does_not_add_duplicate_elements():
    new_set = set()
    new_set.add('item')
    new_set.add('item')
    assert new_set.storage == ['item']

def test_remove_method_removes_element_from_storage():
    new_set = set()
    new_set.add('item')
    new_set.remove('item')
    assert new_set.storage == []

