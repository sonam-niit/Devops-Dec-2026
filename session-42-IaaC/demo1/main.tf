provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "server" {
  ami           = var.amiid
  instance_type = var.instance_type
  key_name = aws_key_pair.example.key_name 
#   key_name connected from below creation
  tags = {
    Name = var.instance_name
  }
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