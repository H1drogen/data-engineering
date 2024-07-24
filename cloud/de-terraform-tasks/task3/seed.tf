resource "aws_db_instance" "sample-server-database" {
  allocated_storage    = 5
  db_name              = "sample-server-database"
  engine               = "postgres"
  engine_version       = "12.4"
  instance_class       = "db.t2.micro"
  username             = "api-db"
  password             = var.api-db-password
  parameter_group_name = "default.postgres12"
  skip_final_snapshot  = true
  vpc_security_group_ids = [aws_security_group.database_sg.id]

}

resource "aws_security_group" "database_sg" {
  name        = "db-security-group"
  description = "Security group for sample-server-database"

  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
