
resource "aws_s3_bucket" "demo_bucket" {
  bucket_prefix = "mybucket"
}

resource "aws_s3_object" "demo_object" {
  bucket = aws_s3_bucket.demo_bucket.id
  source = "test_file.txt"
  key = "test_file.txt"
}
