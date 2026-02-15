class Parent:
    def __init__(self):
        print("Calling parent class Init")
    def stay(self):
        print("Stays in parent house")
        
class Child(Parent): #inheriting form Parent
    def __init__(self):
        super().__init__() # calling parent class constructor
        print("Calling Child class Init")
    def stay(self):
        super().stay() # calling parent class method
        print("Stays in Own house")
        
    def study(self):
        print("Child study going on")
        
        
c1=Child() #creating object of Child
c1.study()
c1.stay()

# Method Overriding happens only in the case when child class and Parent class 
# having same method name same no of parameters then when you call method automatically it
# will oevrride parent class method and using own method