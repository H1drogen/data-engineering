from src.negate import negate
import types

def test_returns_a_function():
    def test_func():
        return True
    output_func=negate(test_func)
    assert type(output_func)==types.FunctionType

def test_returned_function_invokes_original_function():
    def test_func():
        return
    output_func=negate(test_func)
    assert output_func()==True

def test_negates_function():
    def does_this_return_true():
        return True
    output_func=negate(does_this_return_true)
    assert output_func()==False

def test_function_works_as_a_decorator():
    @negate
    def does_this_return_true():
        return True
    assert does_this_return_true()==False