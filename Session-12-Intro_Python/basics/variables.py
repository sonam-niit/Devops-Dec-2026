number = 5 #number  integer
full_name = "sonam soni"
product_price=34.45 # float
is_valid=True #boolean

print("Number: ",number)
print("Full Name: ",full_name)
print("Product Price: ",product_price) # normal concat
print(f"User is Valid? "{is_valid}) # f string

## Multiple Variable in one line

a,b,c = 1,2,3 # means a=1, b=2, c=3
x=y=z=20 #  means x=20, y=20, z=20

print("a:",a," b:",b," c:",c," x:",x," y:",y," z:",z)
# another way to write above code using f string
print(f"a:{a} b:{b} c:{c} x:{x} y:{y} z:{z}")