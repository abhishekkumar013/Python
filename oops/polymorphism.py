# Polymorphism : Operator Overloading
# When the same operator is allowed to have different meaning according to the context.
# Operators & Dunder functions
 

class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def  showNum(self):
        print(f"{self.real}i + {self.img}j")
    
    def add(self,num2):
        numReal=self.real+num2.real
        numImg=self.img+num2.img
        return Complex(numReal,numImg)
    
    def __add__(self,num2):
        numReal=self.real+num2.real
        numImg=self.img+num2.img
        return Complex(numReal,numImg)
    
    def __sub__(self,num2):
        numReal=self.real-num2.real
        numImg=self.img-num2.img
        return Complex(numReal,numImg)
    def __gt__(self,num2):
        return self.real>num2.real
    
num1=Complex(1,3)
num1.showNum()

num2=Complex(2,5)
num2.showNum()

num3=num1.add(num2)
num3.showNum()

num4=num1+num2
num4.showNum()

num5=num1-num2
num5.showNum()

print(num1>num2)