# Linux commands

**ls**

- list directories, files
```bash
ls # just list files and directories
ls -l # list files and directories with details
ls -a # see hidden files
ls --help # provide details of all flags
```

**mkdir**

- used for creating directory
```bash
mkdir developers # Create directory 
mkdir -p develoers/sonam/backup # create nested directories
# if its already exist then also not give any error (-p option)
ls # to check directory created or not
mkdir sonamsoni -v # to see response in terminal
cd developers # move to that folder
mkdir devops linux aws # creating multiple folders at a time

```
**cd**

- used to change directory
- to go to root location: cd ~
- to go to C or D drive inside windows for WSL
- cd /mnt/d/Phsicswalla/
```bash
cd developers/
cd sonam
cd .. # one step back
```
**File/Folder Removal**

```bash
rmdir sonamsoni # this will remove only empty directory
# if you want to remove all filder with all folders
rm -r developers
```

**Create Files**

```bash
touch data.txt # create empty file
rm data.txt # just remove the created file
```

**Current Working Directry**

```bash
pwd
```

**Create and Edit Files**

- to create and edit files we can use vi or nano editor
```bash
vi data.txt # it will create file and open vi editor
# to start typing your content press i (for insert)
# once editing is done press esc key
# type :wq! enter
# w for save file and q! is for exit

# to verify data written or not use cat command
cat data.txt

# Create File using nano editor
nano file.txt
# start typing your data directly
# once its done ctrl+O then press enter then ctrl+x
# to verify
cat file.txt
```

**Create file with just one line data**

```bash
echo "Hello My Name is Sonam" > sonam.txt # create new file
cat sonam.txt
echo "This is another line" >> sonam.txt # update existing file
cat sonam.txt
```

**Copy Files & Move Files**

```bash
mkdir backup
cp file.txt backup/file.txt
#  source-file  destination-file

mv file1.txt backup/file1.txt
mv sonam.txt backup/sonam.txt
```

