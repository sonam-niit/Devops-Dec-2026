# Ansible Roles

- without Roles everything in one playbook file
- with Roles - structure everything like project
    + more reusable
    + clear code structure
    + manage large setups like nginx,DB easily

- create folder project
- go inside folder using terminal
- run brlow command
- ansible-galaxy init httpd
- ansible-galaxy init mysql

- once the role is created you can see the folder structure with multiple files and folders

- in defaults you can mentioned default variables
- you can edit main.yml file

```yml
app_name: My Apache app 
env: Dev
```

- files folder you can keep the files that you wnat to copy or use.
- handlers you can directly put your handlers
- edit handlers main.yml file

```yml
- name: Apache Restart
  service:
    name: httpd
    state: restarted
```

- your main httpd related code should be added under task
- edit tasks/main.yml file

- vars used to define  variables again
- default varible is having low pariority
- vars having high priority means if you declare same name variable at both place it will use vars and override defaults

**Templates**

- they are used for deployment
- in ansible we are using jinja templates

- create one template under templates folder
- index.html.j2 (i am using jija templates)

```j2
<h1>Welcome to {{ app_name }}</h1>
<h2>Environment {{ env }} </h2>
```

- j2 template is reading variables from default

- for deploy edit tasks/main.yml

```yml
- name: Deploy template
  template: 
    src: index.html.j2 # automatically search in template folder
    dest: /var/www/html/index.html
  notify: Apache Restart
```
