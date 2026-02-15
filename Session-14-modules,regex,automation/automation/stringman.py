# Creating Strings
str1="Hello"
str2="World!"
str3='''
    This is my 
    multiline 
    String
'''
print(str3)
print(f"This is my String: {str1} {str2}")

greeting= str1+" "+str2 #concat
print(greeting)
# Repeat String
print((str1+" ")*5)

# String slicing
print(greeting[0:5])
print(greeting[6:])# if end not given it will take value till end

# Replace
print("replace",str1.replace("H","W"))

# convert
print("upperCase: ",str1.upper())
print("lowerCase: ",str1.lower())

# String length
print("Length: ",len(greeting))

# check
print("Python".startswith("Py"))
print("Python".endswith("on"))


print(len("          hello       "))
print(len("          Hello       ".strip()))# removing extra leading and training space

statement="My name is Sonam Soni and I am a content creator"
words=statement.split() # split with space
print("-".join(words))