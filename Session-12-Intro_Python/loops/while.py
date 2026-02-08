num=1

while num<=5:
    print(num)
    num+=1

print("Loop Completed")

# Range in for loop

data= input("Enter your number: ")
num=int(data) # type conversion
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")