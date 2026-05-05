class car:
    def __init__(self):#default constructor 
        self.brand=" "
        self.model=" "
    def __init__(self,brand,model):#Parameterize constructor
        self.brand=brand
        self.model=model
    def __init__(self,brand="honda" ,model="corolla"):#default value constructor
        self.brand=brand
        self.model=model
# car1=car()
# print(car1.brand)
# print(car1.model)
print("\n")
car2=car("Toyora","Civic")
print(car2.brand,car2.model)
