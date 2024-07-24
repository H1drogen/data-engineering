
data "aws_ami" "amzn-linux-2023-ami" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["al2023-ami-2023.*-x86_64"]
  }
}

resource "aws_instance" "example" {
  ami           = data.aws_ami.amzn-linux-2023-ami.id
  instance_type = "t2.micro"
  key_name =   "EC2instance"
  vpc_security_group_ids = [aws_security_group.allow_ssh_and_http.id]
  user_data = file("./script.sh")
  user_data_replace_on_change = true
  tags = {
    Name = "tf-example"
    Team = "Ewan-&-Simon"
    Environment = "Dev"
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

  ingress {
    cidr_blocks = ["0.0.0.0/0"]
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = -1
    cidr_blocks = ["0.0.0.0/0"]
  }

  
}              