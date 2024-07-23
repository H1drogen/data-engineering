'''This module contains the test suite for the
`Cat's Rare Treasures` FastAPI app.'''

from main import app
from fastapi.testclient import TestClient
import pytest
from db.seed import seed_db

@pytest.fixture
def reset_db():
    seed_db()


def test_healtheck_endpoint_returns_200():
    test_client = TestClient(app)
    response = test_client.get('/api/healthcheck')
    assert response.status_code == 200
    assert response.json() == {'message' : 'all ok'}

def test_treasures_endpoint_returns_200_and_data():
    test_client = TestClient(app)
    response = test_client.get('/api/treasures')
    assert response.status_code == 200
    data = response.json()['treasures']
    for s in data:
        assert type(s['age']) == int
        assert type(s['treasure_id']) == int
        assert type(s['colour']) == str
        assert type(s['cost_at_auction']) == float
        assert type(s['shop_name']) == str

def test_age_is_in_ascending_order():
    test_client = TestClient(app)
    response = test_client.get('/api/treasures')
    assert response.status_code == 200
    data = response.json()['treasures']
    i = 0
    while i < len(data) - 1:
        assert data[i]['age'] <= data[i+1]['age']
        i += 1

def test_output_returns_cost_at_auction_in_ascending_order():
    test_client = TestClient(app)
    response = test_client.get('/api/treasures?sort_by=cost_at_auction')
    assert response.status_code == 200
    data = response.json()['treasures']
    i = 0
    while i < len(data) - 1:
        assert data[i]['cost_at_auction'] <= data[i+1]['cost_at_auction']
        i += 1

def test_output_returns_cost_at_auction_in_descending_order():
    test_client = TestClient(app)
    response = test_client.get('/api/treasures?sort_by=cost_at_auction&order=DESC')
    assert response.status_code == 200
    data = response.json()['treasures']
    i = 0
    while i < len(data) - 1:
        assert data[i]['cost_at_auction'] >= data[i+1]['cost_at_auction']
        i += 1

def test_output_returns_gold_items_sorted_by_cost_at_auction_in_descending_order():
    test_client = TestClient(app)
    response = test_client.get('/api/treasures?sort_by=cost_at_auction&order=DESC&colour=gold')
    assert response.status_code == 200
    data = response.json()['treasures']
    i = 0
    while i < len(data) - 1:
        assert data[i]['colour'] == 'gold'
        i += 1

def test_new_treasure_added_to_db(reset_db):
    test_client = TestClient(app)
    test_body = {
        'treasure_name': 'test1',
        'colour': 'testcolour1',
        'age': 1111,
        'cost_at_auction': 9999,
        'shop_id': 1

    }
    response = test_client.post('/api/treasures', json=test_body)
    print(response)
    assert response.status_code == 201
    s = response.json()
    print(s)

    assert type(s[0]['age']) == int
    assert type(s[0]['colour']) == str
    assert type(s[0]['cost_at_auction']) == float
    assert type(s[0]['shop_id']) == int
    assert type(s[0]['treasure_name']) == str


def test_new_treasure_added_to_db(reset_db):
    test_client = TestClient(app)
    test_body = {
        # 'treasure_id' : 3,
        'new_price' : 5.5
        }
    response = test_client.patch('/api/treasures/3', json=test_body)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data == {
        'treasure' : {
        'treasure_id' : 3,
        'treasure_name': 'treasure-b',
        'cost_at_auction': 5.5,
        'age': 13,
        'colour': 'gold',
        'shop_id': 4

    }}

def test_delete_treasure_removes_id_from_database(reset_db):
    test_client = TestClient(app)
    initial_number_of_rows = len(test_client.get('/api/treasures').json()['treasures'])
    response = test_client.delete('/api/treasures/1')
    assert response.status_code == 204
    assert len(test_client.get('/api/treasures').json()['treasures']) < initial_number_of_rows

def test_get_shops_returns_dictionary_with_right_datatypes_and_stock_value(reset_db):
    test_client = TestClient(app)
    response = test_client.get('/api/shops')
    assert response.status_code == 200
    data = response.json()
    for s in data:
        assert type(s['shop_id']) == int
        assert type(s['shop_name']) == str
        assert type(s['slogan']) == str
        assert type(s['stock_value']) == float

def test_get_max_age_filters_out_upper_age():
    return

