#!/bin/bash
echo "update Packages"
sudo apt update -y
echo "Upgrade all packages"
sudo apt upgrade -y
echo "Remove absolute packages"
sudo apt autoremove -y

echo "Your system is Up to Date"