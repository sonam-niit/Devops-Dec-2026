variable1=$(<forloop.sh) # read file and store it in a variable
echo $variable1

variable2=$(cat test.txt) # anothe way
echo $variable2

# process Substitution

diff <(sort file1.txt) <(sort file2.txt)

# compare command output

diff <(ls ~/dirA) <(ls ~/dirB)
# Create 2 directories and 1 file in each with diffrent names 
# check output