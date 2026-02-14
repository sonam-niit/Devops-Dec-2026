class Server: # blue print
    def __init__(self,name,ip): # constructor (used for initialization)
        self.name=name # instance Variable
        self.ip=ip
        self.status="offline"
        
    def start(self): # method
        self.status="Started"
        print(f"Server {self.name}-{self.ip} :: {self.status} ")
        
    def stop(self):
        self.status="Stopped"
        print(f"Server {self.name}-{self.ip} :: {self.status} ")
      
#Creating object from outside the class code  
s1= Server("Prod-Server","192.168.1.10") # s1 is Object
s1.start() #calling method
s1.stop()
s2= Server("Dev-Server","192.168.1.11")
s2.start()
s2.stop()