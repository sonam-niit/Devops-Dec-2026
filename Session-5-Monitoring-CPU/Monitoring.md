# How to work with top Command

- run top in linux terminal
- see the runnning processes
- check top PID
- press k 
- It will ask you to enter process ID: enter that ID 
- press Enter, It  will ask do you want to sent 15/sigterm just press enter
- it will terminate process and you can see you exited from top process.

**If you want to directly exit from top command do ctrl+c**

# Htop Command

- htop is an interactive, enhanced version of top command for doing more real time monitoring.

```bash
# install in ubuntu
sudo apt  install htop -y
#or install in Linux/centOS
sudo yum  install htop -y
# now run 
htop
# you can see output
```
- sort (f6)
- try to sort using diffremt options and see
- select process that you want to kill (like select htop)
- press f9 or click on kill
- enter sigterm signal and process will be terminated.
- for manuall quit use f10
- use f5 to see the tree view.

**Kill ombie Process**

- Zombie appears ion Red color
- use f5 to get the tree view
- zombie you can't delete directly
- kill parent process

**What to Observe to see Memory Leaks**

- check RES is increasing
- check MEM% increasing
- Process which never release Memory watch over a time and observe

- htop use search aand filter option to search and filter process
- thread details using H (press h and check)

