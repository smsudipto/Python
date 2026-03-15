tuple=("sudipto","hoiri","Dulal","sagorika")
print("your list is:",tuple)
for i in tuple:
    print(i)

"""
    tuple support duplicate value.possible to define indexing.it is sorted and immutable.
"""

tuple =("sudipto",45,35,"hori")
print(tuple)
print(type(tuple))


my_tuple = (1, 2, 3, 2, 4)
print(my_tuple)
# print(my_tuple* 30)


my_tuple = (1, 2, 3, 2, 4,2,2)
print(my_tuple)
print(my_tuple[0])
print(my_tuple.count(2))
print(my_tuple.index(3))
print(my_tuple[1:3])
print(my_tuple[1:])
print(my_tuple[-1])
print(len(my_tuple))
print(max(my_tuple))
print(min(my_tuple))
print(sum(my_tuple))

if 1 in my_tuple:
    print("yes ,1 in present this tuple. ")

my_tuple = (1, 2, 3, 2, 4)

# এক লাইনে কন্ডিশনসহ প্রিন্ট (সরাসরি চেক)
print(f"১০ টিউপলে আছে কি? {"yes12" if 10 in my_tuple else "NO12"}")
print(f"২ টিউপলে আছে কি? {'হ্যাঁ' if 2 in my_tuple else 'না'}")

my_tuple = (1, 2, 3, 2, 4)
a,b,c,d,e=my_tuple
print(f"veriable a",{a})
print(f"veriable b",{b})
print(f"veriable c",{c})
print(f"veriable d",{d})
print(f"veriable e",{e})