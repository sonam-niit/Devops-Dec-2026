resource "aws_instance" "web" {
  ami = var.ami_id
  instance_type = var.instance_type

  vpc_security_group_ids = ["sg-0407ad688d4289dfa"]
#   I used my existing Sec Group Id where port 22 and 80 open
  key_name = "pwskills"

  connection {
    type = "ssh"
    user = "ubuntu"
    private_key = file("~/.ssh/pwskills.pem")
    host = self.public_ip
  }
  provisioner "remote-exec" {
    inline = [ 
        "sudo apt update",
        "sudo apt install nginx -y",
        "sudo systemctl start nginx"
     ]

    #  script = "run.sh"
  }
  provisioner "local-exec" {
    when = destroy
    command = "echo Instance is being deleted "
  }
}