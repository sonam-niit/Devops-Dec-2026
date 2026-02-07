# Special Variables

echo "File Name: $0"
# $1, $2 , $3 indicating arguments

echo "Argument 1: $1"
echo "Argument 2: $2"
echo "Argument 3: $3"

# $# No of Arguments
echo "No of Arguments: $#"

# print all
echo "All Arguments: $@"

# Process Id which is used to excute a script
echo "Process Id: $$"

#$? see status code: 0-success 1-some Error
echo "Exit Status: $?"

# try to run: ./special-var.sh  sonam abc 123456