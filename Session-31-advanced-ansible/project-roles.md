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

```bash
ansible-playbook -i inventory.yml playbook.yml
```
- run playbook you can see role frontend executed with nginx installation and copy html code and deployed on ubuntu instance.

- to show dynamic content in browser we can use templates

## Templating in this exsisting role

- go to default and edit main.yml (create default variables)
- under templates folder create index.html.j2
- edit code
- then use this template inside tasks/main.yml

- run playbook again check in browser