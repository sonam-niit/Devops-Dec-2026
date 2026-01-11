# Setting up a permission

- r(read)-4
- w(write)-2
- e(execute)-1

- 744 ==> 7(rwx)(Owner)-4(r__)(Group)-4(r__)(Others)

```bash
# check existing file folders permissoion
cd developers
touch test.txt
ls -l # check permissons
chmod 755 test.txt
chmod 777 demo.txt
```
## Set symbolic permisssions
- u for owner, o for others and g for group
```bash
# add owner execute permission
chmod u+x test.txt
# remove others write permission
chmod o-w test.txt
# add execute permission for group
chmod g+x test.txt
ls -l # verify
``` 
## For changing OwnerShip

```bash
sudo chown root:root file.txt # changing owner and group
sudo chown sonam file.txt # changing owner only
sudo chown :sonam file.txt # changing group only
```