from src.my_queue import Queue


def test_queue_instantiates_with_only_max_size_argument():
    queue = Queue(5)
    assert queue is not None

def test_enqueue_method_adds_item_to_back_storage():
    new_queue = Queue(5)
    new_queue.enqueue('item')
    assert new_queue.storage == {1: 'item'}

def test_enqueue_method_increases_back_property():
    new_queue = Queue(5)
    new_queue.enqueue('item')
    assert new_queue.get_back_count == 1

def test_dequeue_method_removes_item_from_front_storage():
    new_queue = Queue(5)
    new_queue.enqueue('item')
    new_queue.enqueue('item2')
    new_queue.dequeue()
    assert new_queue.storage == {2: 'item2'}

def test_get_quantity_returns_number_of_items_in_queue():
    new_queue = Queue(5)
    new_queue.enqueue('item')
    new_queue.enqueue('item2')
    assert new_queue.get_quantity() == 2

def test_is_empty_returns_true_when_queue_is_empty():
    new_queue = Queue(10)
    assert new_queue.is_empty() == True

def test_is_empty_returns_false_when_queue_is_not_empty():
    new_queue = Queue(10)
    new_queue.enqueue('item')
    assert new_queue.is_empty() == False

def test_is_full_returns_true_when_queue_is_full():
    new_queue = Queue(2)
    new_queue.enqueue('item')
    new_queue.enqueue('item2')
    assert new_queue.is_full() == True

def test_storage_setter_updates_storage():
    new_queue = Queue(10)
    new_queue.storage = {1: 'item'}
    assert new_queue.storage == {1: 'item'}

def test_storage_setter_returns_correct_back_count():
    new_queue = Queue(10)
    new_queue.storage = {1: 'item'}
    assert new_queue.get_back_count == 1

