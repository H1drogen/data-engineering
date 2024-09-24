import os
import time

import pytest
import boto3
from unittest.mock import patch
from moto import mock_aws
from src.password_manager import *

@pytest.fixture(scope="function")
def sm_client():
    with mock_aws():
        yield boto3.client("secretsmanager", region_name="eu-west-2")

class TestMakeSecret:
    pass

class TestListSecrets:
    pass

class TestGetSecret:

    def test_get_secret(self, sm_client):
        sm_client.create_secret(Name='test', SecretString=f'{{"username":"test_id","password":"1234"}}')
        with patch("src.password_manager.client", sm_client):
            get_secret('test', "./test.txt")
            with open("./test.txt", "r") as file:
                result = eval(file.read())
                assert result== {"username":"test_id","password":"1234"}
        os.remove("./test.txt")

class TestDeleteSecret:

    def test_get_secret(self, sm_client):
        sm_client.create_secret(Name='test', SecretString=f'{{"username":"test_id","password":"1234"}}')
        with patch("src.password_manager.client", sm_client):
            delete_secret('test')
            time.sleep(1)
            assert list_secrets() == []