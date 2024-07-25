import pytest
from api.app import client
from fastapi.testclient import TestClient

@pytest.fixture
def reset_db():
    pass

@pytest.mark.it('unit test: healthcheck responds correctly')
def test_handle_healthcheck():
    test_client = TestClient(client)
    response = test_client.get('/healthcheck')
    assert response.status_code == 200

def test_tresures_endpoint_returns_json():
    test_client = TestClient(client)
    response = test_client.get('/doughnuts/info')
    assert response.headers['Content-Type'] == 'application/json'

def test_treasures_endpoint_without_parameters_returns_200_and_all_data():
    test_client = TestClient(client)
    response = test_client.get('/doughnuts/info')
    assert response.status_code == 200
    assert len(response.json()['results']) == 10

def test_treasures_endpoint_with_max_calories_parameter_returns_200_and_filtered_data():
    test_client = TestClient(client)
    response = test_client.get('/doughnuts/info?max_calories=800')
    assert response.status_code == 200
    assert len(response.json()['results']) == 7

def test_treasures_endpoint_with_both_parameters_returns_200_and_filtered_data():
    test_client = TestClient(client)
    response = test_client.get('/doughnuts/info?max_calories=800&allow_nuts=False')
    assert response.status_code == 200
    assert len(response.json()['results']) == 5

def test_treasures_endpoint_with_no_results_returns_204():
    test_client = TestClient(client)
    response = test_client.get('/doughnuts/info?max_calories=100')
    assert response.status_code == 204