data= input("Enter Something:")

if data.isdigit(): # isdigit() is inbuilt function to check input is whole number or not
    print("It is Number")
    print(type(data)) # by default data type of input is string
    num= int(data) # convert it in integer
    print(f"Num: {num}, its DataType: {type(num)}")
else:
    print("Not a Number")