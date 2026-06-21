output "public_ip" {
  value = module.ec2.public_ip
}
output "public_dns" {
  value = module.ec2.public_dns
}
output "instance_id" {
  value = module.ec2.instance_id
}

# showing all results coming from ec2 module externally