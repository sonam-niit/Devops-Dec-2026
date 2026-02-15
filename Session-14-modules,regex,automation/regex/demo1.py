import re

text="Hello from Simple Regex Demo"
pattern=r"Hello"

# i wnat to check Hello is start of my statement
match=re.match(pattern,text)
if match:
    print("Text started with Hello")
else:
    print("Text not started with Hello")
    
# check something from entire string
search= re.search(r"ERROR","This is Log ERROR...")
if search:
    print("text includes Error")
else:
    print("text not includes error")