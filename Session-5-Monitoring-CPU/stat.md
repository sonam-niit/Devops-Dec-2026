# Stastics

1. vmstat stands virtual memory Stastics.
    - reports on processes, Memory Usasge, CPU activity, IO disk
```bash
# run
vmstat # just gives singel output

vmstat 1 # shows result after every 1 sec , use ctrl+c to exit
vmstat 2 5 # run after every 2 sec for 5 times
vmstat 2 5 -SM # showing Memory in MB
```

2. IOstat
    - it reports CPU usage, Device IO, Pratitiondisk throughtput and utilization
    - it is a part of sysstat package
```bash
sudo apt install sysstat
iostat
iostat 2 5
iostat -c # CPusage Only
iostat -d # Device stat Only
iostat -x # Extended stat Only
```

3. PS - process Status

- displays information about currently running processes in your system
- this is same as htop and top but proves snapshot not updating process continously.
```bash
ps
ps aux # a all users. u user/owner , x include processes
ps -u sonam # for perticular user
ps -p 490 # for perticular process id 
```

# Priorities Nice and Renice

- nice is used to start a process with some specified priority
- renice is used to chnage priority of existing process
- each process is having nice value ranging from -20 to 19
- by default when you start a new process the nice value is 0
- you can check using top command as well.
- Prioroty is 20, so if nice is 0 then 20+0 priority is 20
- if nice is -1 the priority is 20+ (-1) = 19
- Higher the value means having low priority
- requires root access to give negative priority

## Demo

```bash
mkdir -p developers
cd developers
nano myscript.sh # we are creating one script file\
# enter below code
```

```bash
echo "Start My Script with Priority $(nice)"
sleep 100
echo "Script finished"
# ctrl+o enter crl+x for exit
#verify entered code
cat myscript.sh

# now Let's Run Script
sh myscript.sh & # run in background
# may be you can see default outout with nice value 0 , ctrl+c
top -p PID # came from above command
# you can see nice value 0 priority 20

# Now Let's Change
sudo renice -10 PID
# enter password and nice value updated
top -p PID # you can see now Priority is 10 nice value is -10
```

## Start Script with Some new priority not default

```bash
nice -n 10 sh myscript.sh & # nice value is 10 means Priority 30
top -p PID # check Priority & NICE
```