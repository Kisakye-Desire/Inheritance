from winreg import REG_NO_LAZY_FLUSH


class Student:
    def __init__(self,regno,name,age):
        self.regno=regno
        self.name=name
        self.age=age
        
    
    
    #Creating functions known as methods     
    def Study(self):
        return"I am studying"
    
    def Play(self):
        return"I am playing"
    
    def Discuss(self):
        return"I am discussing"
    
    def __str__(self):
        return f"My name is{self.name}"
    
student_1=Student("S21B13/04O","Desire",4)
print(student_1)

#Making the function work you have to add brackets e.g print(student_1.Study())
print(student_1.Study())

#Creating a new class to inherit from the parent class
#class NetworkAdmin(Student):
   # def __init__(self,regno,name,age):
       # super().__init__(self,name,age,regno)
        
       # return"I have been created"
    
    
    #def __strt__(self):
       # return f"Name:{self.name}\n Age:{self.age}\n Regno:{self.regno}"
#student_2=NetworkAdmin("J21B13/040",48,"Tom")
#print(student_2.Study)
        