import pytest
from unittest.mock import MagicMock, patch

import cruncher
from cruncher import NumberCruncher, NumberRequester


def test_number_cruncher_likes_even_numbers():
    """Test that the crunch method saves number facts for even numbers.
    
    Given:
         A Number cruncher instance getting an even result for its "crunch" method (eg 42)

    Result:
        Method returns "Yum! 42"
        The tummy attribute contains a dict such as {'number': 42, "fact": "42 is the meaning of life."}
    
    """
    mock_object = MagicMock()
    mock_object.call.return_value = {'result': 'SUCCESS', 'number': 42, "fact": '42 is the meaning of life.'}
    cruncher = NumberCruncher(2, mock_object)
    assert cruncher.crunch() == 'Yum! 42'
    assert cruncher.tummy() == [{'number': 42, "fact": "42 is the meaning of life."}]
    assert len(cruncher.tummy()) == 1


def test_number_cruncher_hates_odd_numbers():
    """Test that the crunch method rejects number facts for odd numbers.
    
    Given:
         A Number cruncher instance getting an odd result for its "crunch" method eg 13

    Result:
        Method returns "Yuk! 13"
        The tummy attribute is unchanged.
    
    """
    mock_object = MagicMock()
    mock_object.call.return_value = {'result': 'SUCCESS', 'number': 13, "fact": '13 is an unlucky number'}
    cruncher = NumberCruncher(2, mock_object)
    assert cruncher.crunch() == 'Yuk! 13'
    assert cruncher.tummy() == []
    assert len(cruncher.tummy()) == 0


def test_number_cruncher_discards_oldest_item_when_tummy_full():
    """Test that the crunch method maintains a maximum number of facts.
    
    Given:
         A Number cruncher instance with tummy size 3 having 3 items in tummy getting 
         an even result for its "crunch" method, eg 24.

    Result:
        Method deletes oldest result from tummy (eg 42)
        Method returns "Burp! 42"
        The tummy attribute contains 24 but not 42.
    
    """
    mock_object = MagicMock()
    mock_object.call.side_effect = [{'result': 'SUCCESS', 'number': 42, "fact": '42 is the meaning of life.'},
                                    {'result': 'SUCCESS', 'number': 42, "fact": '42 is the meaning of life.'},
                                    {'result': 'SUCCESS', 'number': 42, "fact": '42 is the meaning of life.'},
                                    {'result': 'SUCCESS', 'number': 24, "fact": '24 is a very random number'} ]
    cruncher = NumberCruncher(3, mock_object)
    cruncher.crunch()
    cruncher.crunch()
    cruncher.crunch()
    assert cruncher.crunch() == 'Burp! 42'
    assert cruncher.tummy()[2] == {'number': 24, "fact": '24 is a very random number'}



def test_number_cruncher_raises_runtime_error_if_invalid_number_request():
    """Test that there is a runtime error if NumberRequester response is
        invalid

        Given:
            A NumberCruncher instance, receiving an invalid NumberRequester
            response (eg an AttributeError)

        Result: 
            Raises RuntimeError
    """
    mock_object = MagicMock()
    mock_object.call.side_effect = AttributeError('Boom!')
    cruncher = NumberCruncher(3, mock_object)
    with pytest.raises(RuntimeError):
        cruncher.crunch()