output "public_ip" {
  description = "Public IP of an EC2 Instance"
  value = aws_instance.server.public_ip
}
output "public_dns" {
  value = aws_instance.server.public_dns
}
output "instance_id" {
  value = aws_instance.server.id
}