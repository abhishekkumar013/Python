# Methods that don't use the self parameter (work at class level)

# *Decorators allow us to wrap another function in order to
# extend the behaviour of the wrapped function, without
# permanently modifying it

class Student:
    @staticmethod
    def welcome():
        print("Welcome to the Student class")
    
   

s1=Student()
s1.welcome()