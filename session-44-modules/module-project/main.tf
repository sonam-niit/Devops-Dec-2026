provider "aws" {
  region = "us-east-1"
}

module "sg" {
  source = "./modules/sg"
}
module "key-pair" {
  source = "./modules/key-pair"
}
module "ec2" {
  source = "./modules/ec2"
  sec_group_id = module.sg.sec_group_id
#   sec_group_id is coming as output from sg module
  key_name = module.key-pair.aws_key_pair
}