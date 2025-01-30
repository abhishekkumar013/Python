# When one class(childlderived) derives the properties & methods of another class(parentlbase).
# • Single Inheritance
# • Multi-level Inheritance
# • Multiple Inheritance

class Base:
    def __init__(self):
        self.base_attr = "Base attribute"

    @staticmethod
    def base_method():
        print("Base method")
    def base(self):
        print("Base method2")

class Derived(Base):
    def __init__(self):
        super().__init__()
        self.derived_attr = "Derived attribute"
    
    def derived_method(self):
        print("Derived method")

# multilevel
class Derived2(Derived):
    def derived_method2(self):
        print("Derived method2")

#multiple
class Multiple(Derived,Base):
    def multiple_method(self):
        print("Multiple method")

obj = Derived()

# Accessing attributes and methods of derived class

print(obj.base_attr)
obj.base_method()

print(obj.derived_attr)
obj.derived_method()