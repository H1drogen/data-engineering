# Test your implementation here
from src.my_stack import Stack

def test_stack_instantiates_with_empty_values():
    stack = Stack(0)
    assert stack is not None

def test_max_size_returns_default_value_without_specifying():
    new_stack = Stack(0)
    assert new_stack.max_size == 0

def test_push_method_increases_quantity():
    new_stack = Stack(0)
    new_stack.push('item')
    assert new_stack.quantity == 1

def test_push_method_adds_item_to_storage():
    new_stack = Stack(0)
    new_stack.push('item')
    assert new_stack.storage == {1: 'item'}

def test_pop_method_removes_latest_item():
    new_stack = Stack(10)
    new_stack.push('item')
    new_stack.push('item2')
    new_stack.pop()
    assert new_stack.storage == {1: 'item'}

def test_pop_method_returns_latest_item():
    new_stack = Stack(10)
    new_stack.push('item')
    new_stack.push('item2')
    assert new_stack.pop() == 'item2'

def test_is_empty_method_returns_true_when_stack_is_empty():
    new_stack = Stack(10)
    assert new_stack.is_empty() == True

def test_is_empty_method_returns_false_when_stack_is_not_empty():
    new_stack = Stack(10)
    new_stack.push('item')
    assert new_stack.is_empty() == False

def test_is_full_method_returns_true_when_stack_is_full():
    new_stack = Stack(2)
    new_stack.push('item')
    new_stack.push('item2')
    assert new_stack.is_full() == True

def test_peek_method_returns_latest_item():
    new_stack = Stack(2)
    new_stack.push('item')
    new_stack.push('item2')
    assert new_stack.peek() == 'item2'
