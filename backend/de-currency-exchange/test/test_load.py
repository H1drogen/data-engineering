import json
import os
import pytest
from src.load import lambda_handler
import boto3
from moto import mock_aws

@pytest.fixture(scope="function")
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"

@pytest.fixture(scope="function")
def aws(aws_credentials):
    with mock_aws():
        yield boto3.client("s3", region_name="eu-west-2")

@pytest.fixture
def create_bucket1(aws):
    boto3.client("s3").create_bucket(Bucket="nc-de-currency-data-20240805125909831800000003", CreateBucketConfiguration={
        'LocationConstraint': 'eu-west-2'})

@mock_aws()
def test_load_creates_object_in_specified_bucket(create_bucket1):
    event = {"output":
        {
            "eur": {
                "rate": 1.08167213,
                "reverse_rate": 0.924495
            }
        }}
    response = lambda_handler(event, {})
    assert response == {'result': 'Success'}
