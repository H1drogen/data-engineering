import pytest
from unittest.mock import patch
from src.helpers_tasks import get_quote, get_parameter
import boto3
from moto import mock_aws


class TestGetQuote:
    """Tests the get_quote helper."""

    @pytest.mark.it("unit test: get_quote returns correctly formatted dict")
    def test_get_quote_dict(self, sample_quote_list, result_quote_1):
        with patch("src.helpers_tasks.random.choice") as mock_choice:
            mock_choice.return_value = sample_quote_list[0]
            assert get_quote() == (200, result_quote_1)

    @pytest.mark.it("integration test: get_quote gets valid quote")
    def test_get_quote_valid_url(self):
        status_code, _ = get_quote()
        assert status_code == 200

    @pytest.mark.it("unit test: returns correct message if non 200 response")
    def test_get_quote_error_response(self):
        with patch(
                "src.helpers_tasks.random.choice",
                side_effect=Exception("The requested resource could not be found"),
        ):
            status_code, response = get_quote()
            assert status_code == 500
            assert response == {
                "status_message": (
                    "Unexpected error: The requested resource could not be found"
                )
            }


@mock_aws
def test_get_parameter_returns_correct_value():
    conn = boto3.client('ssm')
    conn.put_parameter(Name='test_resource', Type='String', Value='test1')
    assert get_parameter('test_resource') == 'test1'

@mock_aws
def test_get_parameter_throws_client_exception_if_parameter_not_present():
    assert get_parameter('dsd') == 'An error occurred (ParameterNotFound) when calling the GetParameter operation: Parameter dsd not found.'


