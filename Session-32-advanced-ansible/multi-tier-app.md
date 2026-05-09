# Multitier deployment Dem0

- deploying database and application servers in coordinated manners using Ansible
    + Database Setup
    + Application which connect to DB
    + Coordinated all things ansible, handlers, roles, playbooks

- create folder named multi-tier-deployment
- create file inventory.yml
- create file playbook.yml

- create 2 roles:

```bash
ansible-galaxy init roles/db
ansible-galaxy init roles/app
ansible-galaxy init roles/frontend 
# frontend we can create with backend
```
- here we need to setup DB which is Postgre SQL
- app create Python code to connect with DB
- run playbook
- see Db created, APP Deployed and Application is connecting with DB or not