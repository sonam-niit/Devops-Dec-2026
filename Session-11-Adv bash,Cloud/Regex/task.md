# 5 min Task

1. Write a code to take an IP from User
    - create regex to validate
    - if its valid then print IP is valid or not

```bash
#!/bin/bash

read -rp "Enter IP: " data
# pattern='^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$' 
pattern='^[0-2]{1}[1-5]{1}[0-5]{1}\.{3}[0-2]{1}[1-5]{1}[0-5]{1}$' 
if [[ $data =~ $pattern ]]; then
    echo "Valid"
else
    echo "Not Valid"
fi
```

2. Math 8 digits in a raw
```bash
pattern='[0-9]{8}'
```
## Practice Task 
3. Match single a followed by 0 or more b, followd by c
    - ac, abc , abbbbc -- correct
    - abbba , aabc , abbbac -- Incorrect 

