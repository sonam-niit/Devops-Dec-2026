import sys

print("Script Name: ",sys.argv[0])
print("All Arguments: ",sys.argv[1:])

# run using : python3 cmdarg.py sonam 12 true hello.txt

# iterate
for i in sys.argv[1:]:
    print(i)