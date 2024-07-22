from src.convert_type import convert_type
import types

def test_convert_type():
    @convert_type(set)
    def create_simple_list():
        return [1, 1, 2, 2, 3, 4, 5, 5, 5]
        
    assert create_simple_list()=={1, 2, 3, 4, 5}
