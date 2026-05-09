# How Ansible Executes Task

1. Rule1:
    - task run sequencentially (one task at a time)
    - Host run in parrellel (multiple servers at once)

- how ansible things: task1 means execute task 1 on machine1, machine2, machine3....
- run task1 on all hosts and then move to the task2

2. Default Parrellelism:

    - ansible using forks
    - this helps to controll howmany hosts in manages at same time
    - default forks: 5

```bash
ansible-config dump | grep DEFAULT_FORKS
# you can also change it at time of playbook execution
ansible-playbook playbook.yml -f 10
# temporary change
```
3. permanent change then:
    - use ansible.cfg file edit
    - forks=10
    - permanent change.

4. incase if you have 25 servers then playbook executes in batch mode

    - batch1: server1-5
    - batch2: server6-10
    - batch3: server11-15
    - batch4: server16-20
    - batch5: server1-25

## limiting

- to limit playbook execution o n hosts
- eg. inventory

```ini
[web]
server1
server2
server3

[db]
db1
db2
```

- playbook is restrating nginx
- mentioned to run on all hosts
- limiting it

- ansible-playbook playbook.yml --limit server1,server2
- limit on group
- ansible-playbook playbook.yml --limit web 