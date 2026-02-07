#!/bin/bash

read -rp "Enter Something: " data
pattern='^[0-9]+$' # pattern you can store in variable using ''

if [[ $data =~ $pattern ]]; then
    echo "It is an integer number"
else
    echo "Not an integer Number"
fi
# [[....]] advanced Test Command
# =~ cannot work without [[]]
# powerful to test regex