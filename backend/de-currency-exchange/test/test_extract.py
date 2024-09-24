from src.extract import lambda_handler

def test_extract_returns_dictionary():

    response = lambda_handler({}, {})
    assert isinstance(response, dict)

def test_extract_works_correctly():
    response = lambda_handler({}, {})
    assert response['eur']['usd'] > 0