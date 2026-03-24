# class Instructor:
#     def __init__(self):
#         print("Creating a new object.")
#
# instructor_1 = Instructor()
# instructor_1.name="Sudipto Mandal"
# instructor_1.address="Mirpur-2,Rupnagar "
# print(instructor_1.name)
# print(instructor_1.address)
#
# print("\n")
# instructor_2 = Instructor()
# instructor_2.name="HORI Mandal"
# instructor_2.address="Mirpur-11,Rupnagar "
# print(instructor_2.name)
# print(instructor_2.address)

class Instructor:
    def __init__(self,instructor_name ,address,instragram_followrs):
        self.name=instructor_name
        self.address=address
        self.followrs=instragram_followrs



instructor_1 = Instructor("sudipto","Mirpur-11","10k")
print("Name:",instructor_1.name)
print("address:",instructor_1.address)
print("Followers:",instructor_1.followrs)
print("\n")

instructor_2 = Instructor("HORI","Mirpur-1","5k")
print("Name:",instructor_2.name)
print("Address:",instructor_2.address)
print("Followers:",instructor_2.followrs)
print("\n")

instructor_3=Instructor("Sagorika","Tentulbari",0)
print("Name:",instructor_3.name)
print("Address:",instructor_3.address)
print("Followers:",instructor_3.followrs)
print("\n")

instructor_4=Instructor("Dulal","Tentulbari",500)
print("Name:",instructor_4.name)
print("Address:",instructor_4.address)
print("Followers:",instructor_4.followrs)



