# Property
# We use @property decorator on any method in the class to use the method as a property.
class Student:
    def __init__(self, phy,chem,math):
        self.phy = phy
        self.chem=chem
        self.math =math

    def calcPercentage(self):
        self. percentage=((self.phy + self.chem + self.math) / 3) +"%"
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3 )+"%"
    

stul = Student(98, 97, 99)
# stul.calcPercentage()
print(stul.percentage)
stul.phy=70

print(stul.percentage) # It will call the getter method and return the calculated percentage.