# Create Custom AMI

1. create from Existing EC2 instance
    - create one Linux instance.
    - connect with instance
    - execute below commands
```bash
sudo yum update -y
sudo yum install httpd -y
sudo systemctl enable httpd
sudo systemctl start httpd
echo "<h1>Welcome to My Server</h1>" | sudo tee /var/www/html/index.html
```
- verify by public ip or DNS - its working or not
- once its done selct instance and stop.
  
## Create Image AMI

- select instance
- click actions -> Image and templates
- Create Image
- Image name, description and keep default storage settings
- create image
- wait for image cretaion -> check status
- when status is available you can check AMI list with image
- also try to cretae new instance with your Image AMI
