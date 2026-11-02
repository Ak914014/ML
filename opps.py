class Car:

    def price(self, price, nam):
        self.price = price
        self.nam = nam
    
    def total(self):
        print(f"price = {self.nam}, {self.price}")

    @classmethod 
    def hello(cls):
        print("hello")
    
    @staticmethod
    def static():
        print(f"hello ")


cars = Car()
cars.price(233,"hotweels")
cars.total()


# class Animal: 
#     # def __init__(self, name):
#     #     self.name = name
     
#     def nameAnimal(self, name):
#         self.name = name

#     def hello(self):
#         print(f"Name of animal {self.name}")


# class Humnam(Animal):
#     pass

# obj = Humnam("Jenish")
# obj.hello()




class Lion:
    def __init__(self,age,name) :
        self.age = age
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}"
    
    def __add__ (self, other):
        return f"{self.age+ other.age}"


    
obj = Lion(4, "lion")
obj2 = Lion(1,"tiger")

print(obj+obj2)