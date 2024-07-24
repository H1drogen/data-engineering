resource "aws_s3_bucket" "demo_bucket" {
  bucket_prefix = "mybucket"
}

resource "null_resource" "upload_directory" {
  triggers = {
    always_run = "${timestamp()}"
  }

  provisioner "local-exec" {
    command = "aws s3 sync ./sample-server s3://${aws_s3_bucket.demo_bucket.bucket}/de-sample-server"
  }
}

data "aws_s3_bucket" "selected" {
  bucket = aws_s3_bucket.demo_bucket.id
}
