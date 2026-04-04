#we are telling normally function when it defind in class this time we called methode
# class car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
# car1=car("Toyota","corolla")
class car:
    def __init__(self, brand="Toyota", model="Corolla"):
        self.brand=brand
        self.model=model
car1 = car()
print(car1.brand)
print(car1.model)