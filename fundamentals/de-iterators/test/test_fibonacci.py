import time
import pytest
from src.generators.fibonacci import fib

def test_fibonacci_function_returns_first_item():
    fib_gen = fib(1)
    assert next(fib_gen) == 1

def test_fibonnaci_returns_third_iteration():
    fib_gen = fib(3)
    next(fib_gen)
    next(fib_gen)
    assert next(fib_gen) == 3

def test_fibonnaci_returns_iteration_error_if_generation_is():
    fib_gen = fib(3)
    next(fib_gen)
    next(fib_gen)
    next(fib_gen)
    with pytest.raises(StopIteration):
        next(fib_gen)

def test_fibonacci_generates_1000th_sequence_in_less_than_1_second():
    start_time = time.time()
    fib_gen = fib(1000)
    for x in range(1, 1000):
        next(fib_gen)
    assert next(fib_gen) == 70330367711422815821835254877183549770181269836358732742604905087154537118196933579742249494562611733487750449241765991088186363265450223647106012053374121273867339111198139373125598767690091902245245323403501
    assert time.time() - start_time <= 1