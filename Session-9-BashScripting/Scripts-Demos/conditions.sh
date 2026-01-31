#!/bin/bash
# Simple IF
num=10
if [ $num -gt 5 ]
then
    echo "Number is Greater that 5"
fi 

# IF ELSE
name="Test"
if [ $name = "admin" ]
then
    echo "Hello Admin"
else 
    echo "Hello Guest"
fi 

# logicall Operators
echo "Enter your age"
read age
if [ $age -ge 18 ] && [ $age -lt 60 ]
then 
    echo "Eligible Adult"
fi 

echo "Enter Your details"
read user
if [ $user = "admin" ] || [ $user = "root" ]
then    
    echo "you have admin access"
else
    echo "you have normal user access"
fi