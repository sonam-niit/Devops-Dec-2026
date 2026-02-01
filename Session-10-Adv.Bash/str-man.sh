#!/bin/bash

string="Hello, World!"
echo ${string:7:5}
echo ${string:0:5}

message="this is my simple string message"
replace_string=${message//simple/complex}
echo "$replace_string"

echo $string | awk '{gsub(/World/,"Sonam"); print}'

echo "Hello, World World" | sed 's/World/Guest/' # Replace One
echo "Hello, World World" | sed 's/World/Guest/g' # Replace All
# /s substitute String , /g global replace all

# create one text file includes multiple everyone
sed -i 's/everyone/Everyone/g' test.txt #Modify the file
echo "File Modified successfully"
# -i edit file in place