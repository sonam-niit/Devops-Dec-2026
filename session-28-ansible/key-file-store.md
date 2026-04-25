# How to store key file at .ssh location

![sshlocation](images/ssh.png)

*~/.ssh location is secure default place for SSH keys and settings, so SSH can be known where to find your keys and permissions*

```bash
# create directory .ssh folder
mkdir -p ~/.ssh
# move your .pem file at this location
mv /mnt/c/Users/NEW/Downloads/sonamkey.pem ~/.ssh
# set the permission so it will not give publicly available key error
 chmod 400 ~/.ssh/sonamkey.pem
# verify key moved or nor
cat ~/.ssh/sonamkey.pem
# you can see key content
```

