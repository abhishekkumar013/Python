# del keyword
# Used to delete object properties or object itself.
# del sl .name
# del sl
# cannot delete function call

class Student:

    def __init__(self, name):
        self.name = name
    def getname(self):
        print(self.name)

s1=Student("Rammesh")
# print(s1)
# del s1
# print(s1)

# print(s1.name)
# del s1.name
# print(s1.name)

