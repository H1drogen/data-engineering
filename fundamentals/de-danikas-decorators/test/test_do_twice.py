from src.do_twice import do_twice
import types

def test_returns_a_function():
    def test_func():
        return True
    output_func=do_twice(test_func)
    assert type(output_func)==types.FunctionType

def test_returned_function_invokes_original_function():
    def test_func():
        return
    output_func=do_twice(test_func)
    assert output_func()==True

def test_do_twice_function():
    def test_func():
        return
    output_func=do_twice(test_func)
    assert output_func()==True

def test_passing_actual_function():
    def quick_maths():
        2 + 2 - 1 == 3
    output_func=do_twice(quick_maths)
    assert output_func()==True

def test_function_works_as_a_decorator():
    @do_twice
    def quick_maths():
        2 + 2 - 1 == 3
    assert quick_maths()==True
