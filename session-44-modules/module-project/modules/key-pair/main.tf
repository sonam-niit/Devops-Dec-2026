resource "tls_private_key" "example" {
  algorithm = var.algorithm
  rsa_bits  = var.rsa_bits
}
# use Public Key to create Aws Key Pair
resource "aws_key_pair" "example" {
  key_name   = var.key_name
  public_key = tls_private_key.example.public_key_openssh
}

resource "local_file" "private_key" {
  content =  tls_private_key.example.private_key_pem
  filename = var.filename
}