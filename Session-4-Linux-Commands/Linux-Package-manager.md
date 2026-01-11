# Package Management in Linux

- for installing packages you need to update first and then install

```bash
sudo apt update # update
sudo apt install curl # install
curl --version # show you a version of installed package

sudo apt upgrade # new version
sudo apt full-upgrade # upgrade installed dependencies

sudo apt remove curl # just remove installed packages
sudo apt purge curl # just remove installed packages with conf files

sudo apt autoremove # remove unnecessary packages
```

**update**
- download the latest packages from repositories
- it does not install or upgrade any software
- just like refreshing a package-list
**upgrade**
- its actually install newest version of the packages which you already have.
- it compares your installed version with updated package list and then upgrade it.

## System Administration Commands

- systemctl is the main command in system based linux systems.
- control the system service and its state.

```bash
# download apche server
sudo apt install apache2
sudo systemctl start apache2 # start apache service
sudo systemctl status apache2 # check status
# if this service is running i can verify it in browser
# by just checking localhost, you can see default page of apche
sudo systemctl stop apache2 # stop apache service
# start service automatically when you reboot your system
sudo systemctl enable apache2

# you can disable to not start automatically
sudo systemctl disable apache2

sudo systemctl mask apache2 # masking means completly block service
# it will not start manual as well as automatically
# for undo mask
sudo systemctl unmask apache2
#or enable it
sudo systemctl enable apache2
```