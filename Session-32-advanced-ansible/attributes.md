# Attributes in ansible

- ignore_errors: yes (Task Fails but playbook continues)
- failed_when: deside yourself when task should fail

**When to use Failed_when**

- check your custom validation
- fail it based on the output text

- ignore normal command failure:

```yml
- name: Check file
      command: ls /test
      failed_when: 'false
# Task will not fail
# Playbook continous
```

# troubleshoot playbooks

- ansible-playbook failed-when.yml --check
- --check runs playbook in dry-run mode

- use --syntax-check for validating yml syntax

- check verbosity messages while executiong playbook
- for debugging apllication we can use
- ansible-playbook failed-when.yml -v
- ansible-playbook failed-when.yml -vv
- ansible-playbook failed-when.yml -vvv
- ansible-playbook failed-when.yml -vvvv


