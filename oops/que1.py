class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
    def getAvg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print(f"Avg marks {sum/len(self.marks)}")

s1=Student("Abhi",[100,98,100,100,98])
s1.display()
s1.getAvg()