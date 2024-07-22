from src.once import once
import types

def test_returns_a_function():
    def test_func():
        return True
    output_func=once(test_func)
    assert type(output_func)==types.FunctionType

def test_returned_function_invokes_original_function():
    def test_func():
        return 1
    output_func=once(test_func)
    assert output_func()==1

def test_single_invocations_return_correctly():
    def do_some_stuff():
        return "Would you look at that, I've been invoked!"
    output_func=once(do_some_stuff)

    assert output_func()=="Would you look at that, I've been invoked!"

def test_multi_invocations_return_correctly():
    invocation_count=0
    @once
    def do_some_stuff():
        nonlocal invocation_count
        invocation_count+=1
        return "Would you look at that, I've been invoked!"
    
    assert do_some_stuff()=="Would you look at that, I've been invoked!"
    assert do_some_stuff()==None
    assert do_some_stuff()==None
    assert invocation_count==1