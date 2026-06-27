provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "web" {
  ami = var.ami_id
  instance_type = "t3.micro"

  tags = {
    Name = "myapp-${var.env}"
  }
}