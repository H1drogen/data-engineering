from src.s3_tasks import write_file_to_s3, read_file_from_s3

@mock_aws
def test_write_file_to_s3():
    """Test write_file_to_s3 function."""
    # Arrange
    path_to_file = "tests/sonnet18.txt"
    bucket_name = "test-bucket"
    object_key = "sonnets/sonnet18.txt"

    # Act
    result = write_file_to_s3(path_to_file, bucket_name, object_key)

    # Assert
    assert result == "success"