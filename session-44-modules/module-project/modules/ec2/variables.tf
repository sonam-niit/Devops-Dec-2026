variable "amiid" {
  type = string
  description = "Image Id for VM"
  default = "ami-0521cb2d60cfbb1a6"
}
variable "instance_type" {
  type = string
  description = "aws Instance Type"
  default = "t3.micro"
}
variable "instance_name" {
  type = string
  default = "linux-vm"
}
variable "sec_group_id" {
  description = "Security Group ID coming from Module SG"
}
variable "key_name" {
  description = "Key name coming from keypair module"
}