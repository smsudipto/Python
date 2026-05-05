class employ:
    def __init__(self,name ,salary):
        self.name=name
        self._salary=salary #it is define private key but it is actually not private key .it mainly shows golbal access.
    def get_salary(self,password):
        if password=="admin":
            print(self._salary)
        else:
            print("Invalid password.")
    def set_salary(self,password,salary):
        if password=="admin":
            self._salary=salary
            print(f"New Salary:{self._salary}")
        else:
            print("Invalid Access!!!")
obj1=employ("sudipto",30000)
obj2=employ("shojib",20000)

obj1.get_salary("1234")
obj1.set_salary("admin",70000)
