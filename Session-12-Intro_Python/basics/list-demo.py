my_list=[1,2,3,4,5,6,7]
print(my_list)
print(f"Item at index 3: {my_list[3]}")

my_list[2]=33
print(my_list)

# add new
my_list.append(8) # insert at last index
print(f"After Append: {my_list}")
# insert at index
my_list.insert(2,3) # at index 2 insert value 3
print(f"After Insert: {my_list}")
# remove
my_list.remove(33) # remove value
print(f"After Remove: {my_list}")

my_list.pop() # remove last element
print(f"After Remove: {my_list}")

my_list.pop(4) # remove from index 4
print(f"After Remove: {my_list}")

print(f"Length: {len(my_list)}")
# Loop
for num in my_list:
    print(num)
