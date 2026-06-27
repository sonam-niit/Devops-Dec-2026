output "public_ip" {
  description = "Public Ip"
  value = aws_instance.web.public_ip
}