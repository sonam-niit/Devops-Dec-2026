# set is unordered
# no duplicates
# mutable
names={"Alex","Bob","Charlie"}
print(f"Set is: {names}")
names.add("John")
print(f"After Add: {names}")
names.remove("Bob") # throw error if element not exist
print(f"After Remove: {names}")
names.discard("Sonam") # will not throw any error if element not exist
names.add("Alex") # duplicates not allowed
print(f"After Add: {names}")
# how to create empty set
my_set= set() # don't use {} because it creates Dictionary object
my_set.add(1)
print(my_set)