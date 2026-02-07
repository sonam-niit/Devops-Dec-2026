add(){
    local num1=$1
    local num2=$2
    local sum=$((num1+num2))
    echo "The sum of $num1 and $num2 is $sum"
}

#Practice Task
# Create function for SUB, MUL & DIV

echo "Num1: $num1" # cannot access local variable outside function
# call function

add 5 3 # 5 will be stored in $1 and 3 will be stored in $2
