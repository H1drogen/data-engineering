from datetime import datetime as dt

import pytest
from unittest.mock import MagicMock, patch

import cruncher
from cruncher import NumberCruncher, NumberRequester

def test_number_requester_returns_a_valid_result_when_called():
    """Test that the call method returns a valid item.
    
    Given:
         A NumberRequester instance making a successful call

    Result:
        A result as a dict in the form {'result': 'SUCCESS', 'number': 13, "fact": "13 is lucky for some."}

    """
    
    nr = NumberRequester()
    result = nr.call()

    assert isinstance(result, dict)
    assert result['result'] == 'SUCCESS'
    assert 'fact' in result
    assert isinstance(result['number'], int)

@patch('cruncher.requests.get')
def test_number_requester_returns_error_result_for_non_200_response(mock_get):
    """Test that the call method returns a valid item when a request fails.
    
    Given:
         A NumberRequester instance making an unsuccessful call

    Result:
        A result as a dict in the form {'result': 'FAILURE', 'error_code': 404}
    
    """
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    nr = NumberRequester()
    result = nr.call()
    assert result['error_code'] == 404
    assert result['result'] == 'FAILURE'


@patch('cruncher.requests.get')
def test_number_requester_keeps_log_of_requests(mock_get):
    """Test that a NumberRequester instance keeps a log of its own requests.

    Given:
        A NumberRequester is instantiated.
        The NumberRequester.call method is called 5 times at known times.

    Result:
        The NumberRequester.log attribute returns a array of five valid results. Each result
        is a serialisable dict in the form:
        {'request_number': 1, 'call_time': '2022-11-09T16:38:23.417667', 'end_point': 'http://numbersapi.com/random/math',
        'result': 'SUCCESS', 'number': 49}
    Ensure that you test that each dict is exactly correct - including the 'call_time'.
    """

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = '5 this is a cool number'
    mock_get.return_value = mock_response
    nr = NumberRequester()

    with patch('cruncher.dt') as mock_dt:
        mock_dt.now.side_effect = [dt(2024, 8, 1, 15, 19, 27, 12294),
                                   dt(2024, 8, 1, 15, 19, 28, 12294),
                                   dt(2024, 8, 1, 15, 19, 29, 12294),
                                   dt(2024, 8, 1, 15, 19, 30, 12294),
                                   dt(2024, 8, 1, 15, 19, 31, 12294)]

        for number in range(5):
            nr.call()

    assert nr.log == [
        {'request_number': 1, 'call_time': '2024-08-01T15:19:27.012294', 'end_point': 'http://numbersapi.com/random/math', 'result': 'SUCCESS', 'number': 5},
        {'request_number': 2, 'call_time': '2024-08-01T15:19:28.012294', 'end_point': 'http://numbersapi.com/random/math','result': 'SUCCESS', 'number': 5},
        {'request_number': 3, 'call_time': '2024-08-01T15:19:29.012294', 'end_point': 'http://numbersapi.com/random/math','result': 'SUCCESS', 'number': 5},
        {'request_number': 4, 'call_time': '2024-08-01T15:19:30.012294', 'end_point': 'http://numbersapi.com/random/math','result': 'SUCCESS', 'number': 5},
        {'request_number': 5, 'call_time': '2024-08-01T15:19:31.012294', 'end_point': 'http://numbersapi.com/random/math','result': 'SUCCESS', 'number': 5}]




