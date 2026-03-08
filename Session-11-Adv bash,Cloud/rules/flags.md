# Flags

- -e stops script if any command fails
```bash
#!/bin/bash

set -e #EXIT ON ERROR 

echo "starting script"
rm /tmp/non-exist-file # this command will fail
```

- -u stop if you use an undefined variable
```bash
#!/bin/bash
set -u # undefined variable = error

echo "file-deleted"
echo "User is $USERNAME"
```

- -o pipefail fail a pipe if any command in it fails

```bash
#!/bin/bash
set -o pipefail # pipeline fails if any command fails

grep "ERROR" app.log | wc -l
echo "Done"
```
```bash
#!/bin/bash
# Using them together
set -euo pipefail
```