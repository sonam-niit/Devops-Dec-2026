# Ansible Role Project Implemetation

- create folder named full-stack-project
- move to the folder and execute blow commands

```bash
ansible-galaxy role init roles/frontend
ansible-galaxy role init roles/backend
```
- create inventory.yml at root folder
- create playbook.yml at root folder

- go to frontend folder and edit
- tasks/main.yml
- vars/main.yml
- files/index.html (create)
- handlers/main.yml

- run playbook you can see role frontend executed with nginx installation and copy html code and deployed on ubuntu instance.