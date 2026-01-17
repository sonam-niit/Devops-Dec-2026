# Networking

- ifconfig
- part of net-tools package

```bash
sudo apt install net-tools
ifconfig
ifconfig eth0

# change ip
ifconfig eth0 198.168.1.10
# up and down interfaces
ifconfig eth0 down
ifconfig # you can see only one inteface
ifconfig eth0 up
ifconfig
```
# ip command

- alternative of ifconfig command
```bash
ip addr show # or ip a show
ip link show # Showing link
```

*ifconfig is deprecated so use ip*