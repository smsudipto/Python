class Instructor:
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def display(self,subject_name):
        print(f"Hi,I am {instructor_1.name} and I teach  {subject_name}.")

instructor_1=Instructor("sudipto","Tentulbari")
instructor_1.display("Python")
print(instructor_1.name)