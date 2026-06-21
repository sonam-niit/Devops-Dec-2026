resource "aws_instance" "server" {
  ami           = var.amiid
  instance_type = var.instance_type
  vpc_security_group_ids = [var.sec_group_id]
  key_name = var.key_name
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