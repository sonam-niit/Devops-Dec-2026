variable "ami_id" {
  description = "Ubuntu Default Image ID"
  default = "ami-0b6d9d3d33ba97d99"
}
variable "instance_type" {
  type = string
  description = "Type of Instance"
  default = "t3.micro"
}