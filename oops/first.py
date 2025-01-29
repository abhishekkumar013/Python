# To map with real world scenarios, we started using objects in code.
# This is called object oriented programming.
class Student:
   
   #defult constructor
    # def __init__(self):
    #     print("Initialized")
        
    #parametrised constructor
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def getDetail(self):
        print(f"Name: {self.name}, Marks: {self.marks}")
    def getMarks(self):
        return self.marks

s1=Student("Abhi",100) 
print(s1.name )
print(s1.marks)
s1.getDetail()
print(s1.getMarks())
