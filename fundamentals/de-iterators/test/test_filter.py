from src.iterators.filter import NCFilter

def test_filter_strings():
    def check_if_string(val):
        return isinstance(val, str)
        
    x = NCFilter(check_if_string, [1, 'abc', 2, 'def'])
    assert list(x) == ['abc', 'def']