class Person:
    def __init__(self,name,age): # constuctor
        self.name=name
        self.age=age
        # genaral value email, phone, address
    
    def show_details(self):
        print("------------------------------------")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
    def phone(self): # method Oevrriding
        print("Calling from Parent Phone")
        
# Studnet is Child of Person Class
# Student can access all attributes and function of Person class     
class Student(Person):
    def study(self):
        print("Study goind on")
    def phone(self):
        print("Calling from My Own Phone")
        
s1= Student("Sonam","23") # created object of Student class
s1.show_details() # calling parent class method
s1.study() # calling own method
s1.phone()

# if child and father having same function then system automaticlaly call child function and skip
# father function which is called method overriding