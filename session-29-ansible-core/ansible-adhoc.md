# Ansible Adhoc commands 

- these commands are one line commands used to perform quick task on managed node without running entire playbook.

- use it for:
    + ping
    + restart service
    + install single package
    + copy file once
    + gathering system details

```bash
# check connecitivity
ansible all -i inventory.yml -m ping
# run command
ansible server1 -i inventory.yml -m command -a "uptime"
# shell  command
ansible server1 -i inventory.yml -m shell -a "df -h"
# shell  command with piping
ansible server1 -i inventory.yml -m shell -a "df -h | grep /dev"
# install package
ansible server1 -i inventory.yml -m apt -a "name=nginx state=present" -b
# start service
ansible server1 -i inventory.yml -m service -a "name=nginx state=started enabled=true" -b
# -b for sudo use
# check status
ansible server1 -i inventory.yml -m command -a "sudo systemctl status nginx"
```