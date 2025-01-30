# A class method is bound to the class & receives the class as an implicit first argument.
# Note - static method can't access or modify class state & generally for utility.

class Student:
    name="anymous"
    #decorator
    @classmethod
    def change_name(self, name):
        self.name=name
    def change_name2(self, name):
        Student.name=name
    def change_name3(self, name):
        self.__class__.name=name


s1=Student()
s1.change_name("AK")
print(s1.name)
print(Student.name) # but if we not use classmethod then it show default value because that change for only that particular instance(object)