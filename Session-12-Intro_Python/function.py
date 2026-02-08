def greetings():
    print("Hello Everyone!")

def welcome(name):
    if name=='':
        print("Welcome Guest")
    else:
        print(f"Welcome {name}")

def add(num1,num2):
    return num1+num2

greetings() # call function
welcome('') # without name
welcome("Sonam Soni")
result=add(3,4)
print("Result: ",result)
print("Result ",add(5,6)) # calling function in Print
# A function can be defined once and reused multiple times by calling it whenever needed.