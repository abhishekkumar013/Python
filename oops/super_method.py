class Car:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("Car started...")
    
class Toyata(Car):
    def __init__(self, type,brand):
        super().__init__(type)
        self.brand = brand
        super().start()

obj=Toyata("Desiel Engine","Fortuner")
print(obj.type)
print(obj.brand)