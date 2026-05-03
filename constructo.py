#__init__ ,it is dunder method .and it is one kind of constructor 
"""
 mainly three tpe of nonstructor ----------
 1.default constructor
 2.parameterize constructor
 3.default value constructor
 """
# note:jaka amra normally function boli takay amra jokon class ar mordha liki tokon saita hoilo methode
 #2.parameterize constructor
class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
car1=car("Honda","Carola")
print(car1.brand)
print(car1.model)

car2=car("Toyora","Civic")
print(car2.brand,car2.model)

#3.default value constructor
print("\n")
class car:
    def __init__(self,brand="Honda",model="Corola"):
        self.brand=brand
        self.model=model
car1=car()
print(car1.brand)
print(car1.model)

car2=car("Toyora","Civic")
print(car2.brand,car2.model)