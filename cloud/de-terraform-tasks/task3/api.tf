
data "aws_ami" "amzn-linux-2023-ami" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["al2023-ami-2023.*-x86_64"]
  }
}

data "aws_iam_policy_document" "trust_policy" {
  version = "2012-10-17"
  statement {
    effect = "Allow"
    actions = ["sts:AssumeRole"]
    principals {
      identifiers = ["ec2.amazonaws.com"]
      type = "Service"
    }
  }
#   statement {
#   actions   = ["s3:*"]
#   resources = ["arn:aws:s3:::${aws_s3_bucket.demo_bucket.bucket}/*"]
#   effect    = "Allow"
#   }
}

resource "aws_iam_role" "s3_access_role" {
  name = "EC2_S3_Access_Role"
  assume_role_policy = data.aws_iam_policy_document.trust_policy.json
}

# resource "aws_iam_role_policy" "name" {
#   name = "S3AccessPolicy"
#   policy = data.aws_iam_policy_document.s3_access_policy_doc.json
#   role = aws_iam_role.s3_access_role.id
# }

resource "aws_iam_instance_profile" "s3_access_profile" {
  name = "EC2_S3_Access_Profile"
  role = aws_iam_role.s3_access_role.name
}

resource "aws_instance" "fastapi-server" {
  ami           = data.aws_ami.amzn-linux-2023-ami.id
  instance_type = "t2.micro"
  key_name =   "EC2instance"
  vpc_security_group_ids = [aws_security_group.allow_ssh_and_http.id]
  user_data = file("./api_script.sh")
  user_data_replace_on_change = true
  iam_instance_profile = awds_iam_instance_profile.s3_access_profile.name
  tags = {
    Name = "FastAPI server"
    Team = "Ewan-&-Simon"
    Environment = "Dev"
    Purpose = "Deploy API server to cloud"
  }
}

# resource "aws_key_pair" "deployer" {
#   key_name   = "tf-key-pair"
#   public_key = file("/Users/ewanritchie/.ssh/my-key-pair.pub")
# }


resource "aws_security_group" "allow_ssh_and_http" {
  name        = "allow-ssh-and-http"
  description = "Allow SSH and HTTP inbound traffic"
  tags = {
    Description = "Allows HTTP And SSH traffic"
    Association = "EC2 instance - 'example'"
  }
  ingress {
    cidr_blocks = [
      "0.0.0.0/0"
    ]
    from_port = 80
    to_port   = 80
    protocol  = "tcp"
  }

  ingress {
    cidr_blocks = [
      "0.0.0.0/0"
    ]
    from_port = 22
    to_port   = 22
    protocol  = "tcp"
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = -1
    cidr_blocks = ["0.0.0.0/0"]
  }
}    