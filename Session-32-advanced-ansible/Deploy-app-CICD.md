# Deploy Application Ansible + CICD pipeline using Github Actions

- create Seperate Project-folder (ansible-cicd)

## Configure Secrets

![Config Secrets](images/secret-config1.png)

- click on actions, create secrets
![Config](images/config2.png)

- run this command from your Local system where the key stored
- cat ~/.ssh/pwskills.pem   (copy key)

![Create Secret](images/create-secret.png)

![Create Host Secret](images/create-sec2.png)

![UsernameSecret](images/secret3.png)

![AllSecrets](images/all-secrets.png)

- you can push code on Github So workflow will get executed.
- if its executed successfully
- nginx will started on your AWS instance, check in browser with public IP
- you can see default page of NGinx

![Result](images/result.png)

*In your Security group port 80 must open to access output in browser*

- Refer Project Repository Link below
[Reference](https://github.com/sonam-niit/Devops-Dec-ansible-cicd.git)

![App Flow](images/ansible-flow.png)

