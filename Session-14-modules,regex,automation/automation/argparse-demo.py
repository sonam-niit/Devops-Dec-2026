import argparse

parser= argparse.ArgumentParser(description="Simple greeting App")
parser.add_argument("name",help="Enter your Name") # required
parser.add_argument("-a","--age",help="Enter your Age") # optionals
parser.add_argument("-v",'--verbose',action="store_true",help="Enable Verbose Mode")
args= parser.parse_args()

print(f"Hello {args.name}")
if args.age:
    print(f"You are {args.age} years old")
    
# used for creating command line interface

# python3 argparse-demo.py (dont pass anything and see error)
# python3 argparse-demo.py sonam
# python3 argparse-demo.py sonam -a 23 -v
# python3 argparse-demo.py sonam --age 45
