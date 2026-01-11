# Umask

- defines what permission should NOt be set when a new file or directory created.
- masked out permission
- by default:
    - files: 666 (read/write for user/group/others)
    - directory: 777 (read/write/execute for all)

- check current umask value
```bash
umask # you can see 0022
```

**Let's Calsulate**

- default file permission 666 - 022 = 644 (rw_r__r__)
- default directory permission 777 - 022 = 755 (rwxr_xr_x)

**Let's Update Umask Value**

```bash
umask 007
mkdir testmask
cd testmask
mkdir demo
touch hello.txt
ls -l
```
- default file permission 666 - 007 = 660 (rw_rw____)
- default directory permission 777 - 007 = 770 (rwxrwx__)

### Practice Task (do it later)

- calculate file permission and Dir Permission
- umask 000, umask 077, umask 002
