# Dictionary Stores values in Key-value pair
# Values can be anything
# Keys are unique
# Mutable

my_dict={
    "name":"Sonam",
    "age":56,
    "city":"Mumbai"
}

print(my_dict)
my_dict["email"]="sonam@gmail.com" # add new field
my_dict["age"]=35 # Update

print(f"Updated: {my_dict}")

#Iterate
for key,value in my_dict.items(): # for only keys use my_dict.keys(), for values  my_dict.values()
    print(f"{key}: {value}")

#Remove
my_dict.pop("age")
print(f"After Delete: {my_dict}")
del my_dict["city"]
print(f"After Delete: {my_dict}")
my_dict.clear() # remove everything
print(f"After Clear: {my_dict}")

## Snake Case
# first_name, server_status