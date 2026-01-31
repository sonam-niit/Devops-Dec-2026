#!/bin/bash
myname="Sonam Soni" #declare and assigne value to variable
echo "My Name is $myname" # access variable

age=45
echo "Age is $age"

app=Nginx
port=80

echo "Installing $app"
echo "$app is running on port $port"

# Taking input form User
echo "Enter your username"
read username
echo "Username is $username"
# Math Operations
num1=10
num2=20
echo "Sum = $((num1+num2))" # $(()) for Math operation

# today=$(date) # Variable Declaration
echo "Today is $(date)"
echo "Today is $(date +%Y-%m-%d)" # Date Formatting