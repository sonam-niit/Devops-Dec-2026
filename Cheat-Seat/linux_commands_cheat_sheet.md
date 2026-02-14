# Linux Commands Cheat Sheet

------------------------------------------------------------------------

## BASIC NAVIGATION

pwd\
Print current directory path

ls\
List files and folders

ls -l\
List with details

ls -a\
Show hidden files

cd directory_name\
Change directory

cd ..\
Move one level up

cd \~\
Go to home directory

clear\
Clear terminal screen

------------------------------------------------------------------------

## FILE AND DIRECTORY MANAGEMENT

mkdir folder_name\
Create directory

rmdir folder_name\
Remove empty directory

rm file_name\
Delete file

rm -r folder_name\
Delete directory recursively

cp source destination\
Copy file

cp -r source_dir destination_dir\
Copy directory

mv old_name new_name\
Move or rename

touch file_name\
Create empty file

------------------------------------------------------------------------

## FILE VIEWING AND EDITING

cat file\
Show full file content

less file\
View file page by page

head file\
Show first 10 lines

tail file\
Show last 10 lines

tail -f file\
Live log view

nano file\
Open file in nano editor

vi file\
Open file in vi editor

------------------------------------------------------------------------

## SEARCHING

find /path -name filename\
Find file by name

grep "text" file\
Search text in file

grep -r "text" folder\
Search text in directory

which command\
Show command location

------------------------------------------------------------------------

## PERMISSIONS

ls -l\
View permissions

chmod +x file\
Add execute permission

chmod 755 file\
Set numeric permission

chown user file\
Change owner

chown user:group file\
Change owner and group

------------------------------------------------------------------------

## PROCESS MANAGEMENT

ps\
Show running processes

ps aux\
Detailed process list

top\
Live process monitor

htop\
Advanced process monitor (if installed)

kill PID\
Kill process by id

kill -9 PID\
Force kill process

------------------------------------------------------------------------

## SYSTEM INFORMATION

whoami\
Current user

id\
User and group id

uname -a\
System info

hostname\
Show hostname

uptime\
System uptime

date\
Current date and time

------------------------------------------------------------------------

## DISK AND MEMORY

df -h\
Disk usage

du -sh folder\
Folder size

free -m\
Memory usage

lsblk\
List disks

mount\
Show mounted drives

------------------------------------------------------------------------

## NETWORK

ip a\
Show IP address

ping host\
Test connectivity

curl url\
Fetch URL content

wget url\
Download file

ssh user@host\
SSH login

scp file user@host:/path\
Copy file over SSH

------------------------------------------------------------------------

## PACKAGE MANAGEMENT

### Ubuntu / Debian

apt update\
apt upgrade\
apt install package\
apt remove package

### RHEL / CentOS / Amazon Linux

yum install package\
yum remove package

------------------------------------------------------------------------

## ARCHIVE AND COMPRESSION

tar -cvf file.tar folder\
Create tar

tar -xvf file.tar\
Extract tar

tar -czvf file.tar.gz folder\
Create tar.gz

tar -xzvf file.tar.gz\
Extract tar.gz

zip file.zip file\
Create zip

unzip file.zip\
Extract zip

------------------------------------------------------------------------

## HELP

man command\
Manual page

command --help\
Quick help

------------------------------------------------------------------------
