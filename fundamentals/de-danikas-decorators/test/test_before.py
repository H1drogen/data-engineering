from src.before import before
import types

def test_before():
    @before(4)
    def greet():
        return 'Hello there!'
    assert greet()== 'Hello there!'
    assert greet()== 'Hello there!'
    assert greet()== 'Hello there!'
    assert greet()==None
    assert greet()==None