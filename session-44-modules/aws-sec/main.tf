provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "server" {
  ami           = var.amiid
  instance_type = var.instance_type
  key_name = aws_key_pair.example.key_name 
  vpc_security_group_ids = [aws_security_group.web_sg.id]
#   key_name connected from below creation
  tags = {
    Name = var.instance_name
  }
  user_data = <<-EOF
  #!/bin/bash
  yum install httpd -y
  systemctl enable httpd
  systemctl start httpd
  EOF
}

# Create Key Pair

# create Public Private Key Pair
resource "tls_private_key" "example" {
  algorithm = "RSA"
  rsa_bits  = 4096
}
# use Public Key to create Aws Key Pair
resource "aws_key_pair" "example" {
  key_name   = "example-key"
  public_key = tls_private_key.example.public_key_openssh
}

resource "local_file" "private_key" {
  content =  tls_private_key.example.private_key_pem
  filename = "example-key.pem"
}

# Security Group

resource "aws_security_group" "web_sg" {
  
  name = "web-sg"
  description = "Allow HTTP and SSH"

  ingress {
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }
  ingress {
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }
  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }
}