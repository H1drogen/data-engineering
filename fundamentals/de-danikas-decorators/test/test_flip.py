from src.flip import flip
import types

def test_returns_a_function():
    def test_func():
        return True
    output_func=flip(test_func)
    assert type(output_func)==types.FunctionType

def test_returned_function_invokes_original_function():
    @flip
    def test_func(a, b):
        return a+b
    result=test_func(2, 4)
    assert result==6


def test_returned_function_functions():
    @flip
    def divide(a, b):
        return a/b
    assert divide(4, 4)==1
    
def test_returned_function_is_flipped():
    @flip
    def divide(a, b):
        return a/b
    assert divide(2, 4)==2