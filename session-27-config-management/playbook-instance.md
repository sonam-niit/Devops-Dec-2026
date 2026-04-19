# Run Playbook on AWS instance

- create one AWS ubuntu instance
- AWS Console -> EC2 -> launch instance
- select ubuntu
- instance type - t2.micro / t3.micro
- create new key -> give name -> select RSA -> pem -> create
- network -> create new edit -> by default ssh is already there
- add one more rule for port 80 , select HTTP 
- default storage size 8 gb 
- launch instance

## Create inventory.yml

```yml
all:
  hosts:
    server1:
      ansible_host: <public_ip> # public ip of instance
      ansible_user: ubuntu
      ansible_ssh_private_key_file: <give_your_created_key_name>
      # SSH connect we need password
```

## Create Playbook.yml

```yml
- name: Web Server Connect
  hosts: server1

  tasks:
   - name: Ping my hosts
     ansible.builtin.ping:

```

- run command
- sudo ansible-playbook playbook.yml -i inventory.yml

(means run the playbook on mentioned vm inside inventory)

- it will try to connect to your host.

- right noe for quick access keep your pem file at the same folder where inventory and playbook created later i will show you how to secrely keep in inside .ssh folder.
