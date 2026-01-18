# Batch Mode in Top

- Batch mode run witout any user interactions
- just prints standard output

```bash
top -b # runs continously prints output

top -b -n 1 # run for limited iterations
top -b -n 5
top -b -n 5 > output.txt # save output to text file

top -b -d 5 >> top.log # continuous logging, runs every 5 seconds
```


# Swap Usage

```bash
echo 10 | sudo tee /proc/sys/vm/swappiness
# sets linux swappiness to 10, telling kernel to avoid swapping unless really necessary

 cat /proc/sys/vm/swappiness # check Swappiness

 # When you reboot the system this will reset, its temp change

```

## What is swappiness?

- swappiness controls how aggressively linux moves memory pages from RAM to swap
- Value Rage between 0 - 100

- 0 - SWAP only if the RAM almost full
- 10 - very low swapping (suggested for servers)
- 60 - default on most of distributions
- 100 - aggressive swapping

