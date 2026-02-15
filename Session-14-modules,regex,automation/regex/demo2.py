import re

text= "contact me at dev@pw.com or admin@pw.org or sonam.soni@pw.com"
pattern=r"[A-Za-z0-9._-]+@[A-Za-z0-9._-]+\.[A-Za-z]{2,3}"
#Pattern for Email
emails= re.findall(pattern,text)
# find all values which match with this pattern given in text
print(emails)