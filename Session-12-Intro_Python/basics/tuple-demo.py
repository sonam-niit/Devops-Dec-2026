#ordered
#immutable (cannot be changed)
# allows duplicate values

numbers=(10,20,30)
print(f'tuple: {numbers}')

t1=(10,)# for single value , mandatory

print(f"acces based on index: {numbers[2]}")
# numbers[1]=99 # this line will give error 

server = ("web1","10.0.0.1","running") 
# unpacking of tuple
name,ip,status=server
print(f"Name: {name}, IP: {ip}, Status: {status}")